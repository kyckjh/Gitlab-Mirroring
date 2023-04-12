from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-pk')
    context = {'todos':todos}
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == "POST":
        # request에서 데이터 받아와서 DB에 저장
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm(data=request)
    context = {'form':form}
    return render(request, 'todos/create.html', context)
        # todo를 입력할 수 있는 화면 보여주기

def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = { 'todo':todo }
    return render(request, 'todos/detail.html', context)

@require_POST
def update(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.author == request.user:
        todo.completed = not todo.completed
        todo.save()
        return redirect('todos:detail', todo.pk)
    else:
        return redirect('todos:index')