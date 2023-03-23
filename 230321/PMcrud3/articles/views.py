from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModel

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)    
    context = {'article':article}
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method=='POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        form = ArticleModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleModel()
    context = {'form':form}
    return render(request, 'articles/create.html', context)
    
def update(request, pk):
    article = Article.objects.get(pk=pk) 
    if request.method=='POST':
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        form = ArticleModel(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)        
    else:   
        #context = {'article':article}
        form = ArticleModel(instance=article)
    context = {'form':form, 'article':article}
    return render(request, 'articles/update.html', context)

def delete(request, pk):    
    article = Article.objects.get(pk=pk)    
    article.delete()
    return redirect('articles:index')
