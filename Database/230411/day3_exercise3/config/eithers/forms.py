from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = (
            'question',
            'user',
        )
