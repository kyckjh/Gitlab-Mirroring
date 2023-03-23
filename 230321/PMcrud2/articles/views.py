from django.shortcuts import render, redirect
from .models import Article
# from django.core.files.storage import FileSystemStorage
from .forms import ArticleForm

# Create your views here.

# 클라이언트에서 던진 데이터를 받아서, DB에 저장하기
def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # # fs = FileSystemStorage()
        # # file = request.FILES.get('file')
        # # file_url = fs.save(file.name, file)
        # article = Article(title = title, content = content)
        # # article.image = file_url
        # # 저장하기
        # article.save()
        # return redirect('articles:index')
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # return render(request, 'articles/create.html')
    # GET 요청 받으면 form 객체 만들어서 템플릿에 넣어주기
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request, 'articles/create.html', context)

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

# 게시글 하나의 상세정보를 담고 있는 상세 페이지 보여주기
def detail(request, pk):
    article = Article.objects.get(pk=pk) # 앞의 pk 는 keyword argument
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

# 수정 정보 받아서 DB 수정하고 상세화면 보여주기
def update(request, pk):
    article = Article.objects.get(pk=pk) # 앞의 pk 는 keyword argument
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', pk)
    else:
        context = {
            'article':article
        }
        return render(request, 'articles/update.html', context)
    
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk) # 앞의 pk 는 keyword argument
        article.delete()
    return redirect('articles:index')