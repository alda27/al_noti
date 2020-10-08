from .models import Profile
from django.contrib.auth.models import User
from django import forms


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        labels = {
            'first_name': ('Nombres'),
            'last_name': ('Apellidos'),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)
        labels = {
            'photo': ('Foto de Perfil')
        }