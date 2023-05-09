from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иван"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иванов"}))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иванович"}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "ул. Мира, дом 6, кв. 45"}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иркутск"}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': "664000"}))
    telephone = PhoneNumberField(region="RU", widget=RegionalPhoneNumberWidget(attrs={
        'placeholder': "+79248347257"}))
    order_notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)
    basket_history = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'surname', 'address', 'city', 'zipcode',
                  'telephone', 'order_notes', 'basket_history')
