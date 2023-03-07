from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostFormulario(forms.Form):

    title = forms.CharField()
    intro = forms.CharField()
    body = forms.CharField()

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='User Name', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat your Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}