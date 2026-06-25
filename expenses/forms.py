from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            'event',
            'expense_type',
            'amount',
            'expense_date',
            'description',
        ]

        widgets = {

            'event': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'expense_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'expense_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }