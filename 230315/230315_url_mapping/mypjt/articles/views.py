from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def hello1(request, name, score):    
    return render(request, 'articles/index.html', {'name':name, 'score':score})

# def hello2(request, score):    
#     return render(request, 'articles/index.html', {'score':score})