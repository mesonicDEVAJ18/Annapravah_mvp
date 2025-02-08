from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_type', 'quantity', 'expiry_date', 'current_location', 'manual_location']