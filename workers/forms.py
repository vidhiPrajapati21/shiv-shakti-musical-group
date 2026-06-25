from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):

    class Meta:

        model = Worker

        fields = '__all__'

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Worker Name'
                }
            ),

            'mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Mobile Number'
                }
            ),

            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Daily Salary'
                }
            ),

        }