from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    # 최신글 순서로 정렬하기
    articles = Article.objects.all()[::-1]
    # articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # request.GET은 dict
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk) # 기존 내용

    article.title = request.POST.get('title') # 새로 입력한 title을 기존 데이터에 덮어쓰기
    article.content = request.POST.get('content') # 새로 입력한 content를 기존 데이터에 엎어쓰기
    article.save() # DB에 데이터 저장
    return redirect('articles:detail', article.pk)
    

