from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 어떤 형태의 데이터를 입력받을 건지 선언
    # Model Article이 가지고 있는 field 이용해서 선언
    class Meta:
        model = Article
        fields = '__all__'