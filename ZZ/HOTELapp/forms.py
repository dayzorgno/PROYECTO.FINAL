from django import forms
from .models import Buffet

class BuffetReservationForm(forms.ModelForm):
    class Meta:
        model = Buffet
        fields = ['horario', 'menu']