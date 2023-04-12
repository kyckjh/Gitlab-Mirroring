from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from random import randint

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = { 'questions':questions }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = { 'form':form }
    return render(request, 'eithers/create.html', context)

def random(request):
    questions = Question.objects.all()
    count = questions.count()
    rand = randint(1, count)
    redirect('eithers:detail', rand)
    

def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

def comment(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    question = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', question.pk)