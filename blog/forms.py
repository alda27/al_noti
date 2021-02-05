from django.forms import ModelForm
from .models import Comment
from django import forms
from .models import Article


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'photo', 'tags', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple()
        }
