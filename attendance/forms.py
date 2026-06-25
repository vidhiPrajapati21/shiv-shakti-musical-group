from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            'worker',
            'event',
            'date',
            'status',
            'salary'
        ]

        widgets = {

            'worker': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'event': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Salary'
                }
            ),

        }