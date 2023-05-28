from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Your full name please',
            'email': 'Your email address (the real one!)',
            'phone_number': 'Phone number (we know, who calls anyone anymore?)',
            'country': 'Country you want this delivered to',
            'postcode': 'Post Code to locate you',
            'town_or_city': 'Town or City to deliver to',
            'street_address1': 'Street Address 1 (Flat number, House number)',
            'street_address2': 'Street Address 2 (Street name, Custom house name(fancy!)',
            'county': 'County (same as city name if youre lucky',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
