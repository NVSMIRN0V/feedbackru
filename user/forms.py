from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Create a username'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email address'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Create a password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm a password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
