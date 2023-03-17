from django.urls import path
from . import views # 나와 같은 패키지의 views 가져오기

app_name = 'pages'
urlpatterns = [    
    path('index/', views.index, name='index'),
]
