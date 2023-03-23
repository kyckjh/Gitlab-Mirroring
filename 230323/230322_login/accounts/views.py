from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    #GET 요청을 받으면 화면 보여주기
    #POST 요청을 받으면 로그인 처리하기
    if request.method == 'POST':
        #로그인 처리
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:   # GET 요청이라면 로그인 화면보여주기
        #django.contrib.auth.forms.AuthenticationForm
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('articles:index')
    
def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/update.html', context)

def password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/password.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
