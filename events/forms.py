from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [
            'event_type'
        ]

        widgets = {

            'event_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

        }