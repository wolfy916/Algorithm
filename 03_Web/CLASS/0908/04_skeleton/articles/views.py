from .models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


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
    # 5. create 요청을 보냄(POST) => 사용자가 데이터를 입력하고, 저장해달라고 요청 (잘못됨..)
    # 10. create 요청을 보냄(POST) => 사용자가 데이터를 입력하고, 저장해달라고 요청 (올바른)
    if request.method == 'POST':
        # 6. ArticleForm 인스턴스화 (사용자가 입력한 정보 + 빈종이) => 데이터가 입력된 종이 만들기.
        # 11. ArticleForm을 인스턴스화 (사용자가 입력한 정보 + 빈종이) => 데이터가 입력된 종이 만들기.
        form = ArticleForm(request.POST)
        # 7. 데이터가 유효한지 검증한다(잘못된 데이터라 실패!)
        # 12. 데이터가 유효한지 검증한다(올바른 데이터라 성공!)

        if form.is_valid():
            # form.save()
            # return redirect('articles:index')
            # 13. 데이터를 저장한다.
            article = form.save()
            # 14. 원하는 경로로 redirect 시킨다.
            return redirect('articles:detail', article.pk)


    else: # 1. 사용자가 create 경로로 요청을 보냄(GET) => 빈종이 달라!! 요청
        # 2. ArticleForm으로 빈종이 만든다.
        form = ArticleForm()
    # 3. 사용자에게 빈종이를 보내주기 위해서 context 담기
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 담기.
    context = {
        'form': form,
    }
    # 4. 사용자에게 빈종이를 넘겨준다.
    # 9. 사용자에게 올바른 데이터만 있는 종이를 다시 넘겨준다.
    return render(request, 'articles/create.html', context)
    

@require_safe # get 요청만
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # Get..
        form = ArticleForm(instance=article) # 원본이 있어야 되니까 instance로 원본 보내줌
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)



