from django import forms
from django.core.validators import RegexValidator
from django.forms import MultipleChoiceField

from orders.cities import cities
from orders.models import Order


class OrderForm(forms.ModelForm):
    fio = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иванов Иван Иванович"}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "ул. Мира, дом 6, кв. 45"}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иркутск"}))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{11}$")
    telephone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "+79248347257"}),
        validators=[phoneNumberRegex], max_length=16)
    order_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)
    basket_history = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    class Meta:
        model = Order
        fields = ('fio', 'address', 'city', 'telephone', 'order_notes', 'basket_history')

class CdekForm(forms.ModelForm):
    city = MultipleChoiceField(choices=cities, initial='Москва')
    class Meta:
        model = Order
        fields = ('fio', 'address', 'city', 'telephone', 'order_notes', 'basket_history')

