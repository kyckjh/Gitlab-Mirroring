"""mypjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from articles import views as articles_views
# from pages import views as pages_views

urlpatterns = [    
    path('admin/', admin.site.urls),
    # path('articles/index/',articles_views.index),
    # 위처럼 이곳 하나의 urls.py에서 모든 url(/index)들을 처리하지 않고 
    # 아래처럼 articles로 들어오면 articles.urls로 보내서 따로 나눠서 처리하게 하기
    path('articles/', include('articles.urls')),
    # path('pages/index/',pages_views.index),
    path('pages/', include('pages.urls')),
]
