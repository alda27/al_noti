from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Tag, Category
from .models import News


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar una '
                                                                                                  'noticia...'}))


class CreateNewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'preview_content', 'body', 'tags', 'category',
                  'photo', 'is_popular', 'publish', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia'}),
            'preview_content': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Contenido previo de la noticia'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect()
        }


