from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите имя пользователя"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите пароль еще раз"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите ваше имя (Не обязательно)"}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group',
        'placeholder': "Введите вашу фамилию (Не обязательно)"}), required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

