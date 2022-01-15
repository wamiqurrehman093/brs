from django import forms
from .models import Ticket, Bus

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'bus', 'booked_seats')

class SearchForm(forms.Form):
    query = forms.CharField()