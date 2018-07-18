from django import forms
from .models import Metro, Arrival

class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=Metro.objects.all(), label="City")
    arrival = forms.ModelChoiceField(queryset=Arrival.objects.all(), label="Arrival Location")
    check_in = forms.DateField(label="Check In Date")
    check_out = forms.DateField(label="Check Out Date")
