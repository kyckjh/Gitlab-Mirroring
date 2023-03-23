from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, "articles/index.html", context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request, "articles/detail.html", context)

def create(request):
    if request.method=='POST':        
        form = ArticleForm(data=request.POST) # data= 생략 가능 (data가 가장 처음 인자)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>>>>>>')
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request, "articles/create.html", context)
    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request, "articles/update.html", context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")