from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from user.models import Avatar

class UserForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=30, min_length=8, label='Password')
    nick = forms.CharField(max_length=20, label='Nick')

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name' ]
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )