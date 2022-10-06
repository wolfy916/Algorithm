from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all() # 해당 게시글의 달린 댓글을 모두 불러옴
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()
#     return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:  # 현재 사용자와 게시글을 작성한 사용자를 비교하여 본인 글만 수정할 수 있도록 함
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:  # 인증된 사용자인 경우만 댓글 작성 가능
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save() 메서드의 commit=False 옵션으로 저장하기 전에 객체에 대한
            # 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해줌
            comment = comment_form.save(commit=False)
            # DB에 저장하기 전에 article 객체, user 저장
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:  # 인증된 사용자인 경우만 댓글 삭제 가능
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:  # 현재 사용자와 게시글을 작성한 사용자를 비교하여 본인 글만 삭제할 수 있도록 함
            comment.delete()
    return redirect('articles:detail', article_pk)
