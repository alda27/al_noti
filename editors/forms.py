from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'photo', 'tags', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }