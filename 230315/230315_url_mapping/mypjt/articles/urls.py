from django.urls import path
from . import views # 나와 같은 패키지의 views 가져오기

app_name = 'articles'
urlpatterns = [    
    path('index/', views.index, name='index'),
    # path('hello/<str:name>/', views.hello1, name='hello1'),
    # path('hello/<int:score>/', views.hello2, name='hello2'),

    path('hello/<str:name>/<int:score>/', views.hello1, name='hello1'),
]
