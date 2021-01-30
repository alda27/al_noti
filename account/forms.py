from .models import Profile
from django.contrib.auth.models import User
from django import forms


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        # labels = {
        #     'first_name': ('Nombres'),
        #     'last_name': ('Apellidos'),
        # }
        # error_messages = {
        #     'first_name': {
        #         'min_length': ('No puede quedar vacío'),
        #     }
        # }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('photo',)
        # labels = {
        #     'photo': ('Foto de Perfil',)
        # }


#
# class UserEditForm(forms.Form):
#     first_name = forms.CharField(label="Tu nombre", max_length=100)
#     last_name = forms.CharField(label="Tu apellido", max_length=100)
#
#
# class ProfileEditForm(forms.Form):
#     photo = forms.ImageField(label="Tu foto de perfil")


