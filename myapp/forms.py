from django import forms
from .models import Donation, Request

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_type', 'quantity', 'expiry_date', 'current_location', 'latitude', 'longitude']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'food_type': 'Food Type',
            'quantity': 'Quantity (kg)',
            'expiry_date': 'Expiry Date',
            'current_location': 'Location',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['location', 'latitude', 'longitude', 'quantity', 'preferred_datetime', 'food_type', 'special_instructions']
        widgets = {
            'preferred_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'special_instructions': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'location': 'Location (Where food is needed)',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'quantity': 'Quantity (kg)',
            'preferred_datetime': 'Preferred Date and Time',
            'food_type': 'Type of Food Needed',
            'special_instructions': 'Special Instructions',
        }