from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm

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


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-group',
        'readonly': True}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-group',
        'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group',
                                                               'placeholder': "Ваше имя"}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group',
                                                              'placeholder': "Ваша фамилия"}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group',
                                                            'placeholder': "Адрес"}), required=False)
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-group',
                                                               'placeholder': "Почтовый код"}), required=False)
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group',
                                                              'placeholder': "Телефон"}), required=False)

class UserResetPassForm(ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-group',
        'placeholder': "Email"}))

    class Meta:
        model = User
        fields = ('email',)
