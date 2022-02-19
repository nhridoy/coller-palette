from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import models


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = models.User
        fields = '__all__'
