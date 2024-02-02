from django.forms import ModelForm,TextInput
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields=['name','date','time']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your name'}),
            'date': TextInput(attrs={'placeholder': ' YYYY-MM-DD'}),
            'time': TextInput(attrs={'placeholder': 'HH:MM'}),
        }