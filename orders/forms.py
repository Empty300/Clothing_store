from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иван"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иванов"}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "ул. Мира, дом 6"}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Иркутск"}))
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': "Почтовый код"}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Телефон"}))
    order_notes = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':15}), required=False)
    basket_history = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), required=False)

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'city', 'zipcode', 'telephone', 'order_notes', 'basket_history')
