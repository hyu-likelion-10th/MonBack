from dataclasses import fields
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        # Comment라는 모델을 기반으로 입력값을 받을 거야!
        model = Comment
        fields =  ['comment']

