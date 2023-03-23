from django.forms import ModelForm
from django import forms
from .models import Article
class ArticleForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'제목을 입력하세요',
                
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'