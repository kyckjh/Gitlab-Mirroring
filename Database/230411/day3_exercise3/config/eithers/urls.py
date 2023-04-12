from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('random/', views.random, name='random'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/', views.comment, name='comment'),
]
