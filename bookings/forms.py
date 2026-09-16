from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            'customer_name',
            'mobile',
            'address',
            'event',
            'event_date',
            'timing',              
            'dholi',      
            'custom_dholi_count',  # કસ્ટમ ઢોલ સંખ્યા માટેનું નવું ફીલ્ડ
            'sound_type',
            'custom_sound_count',
            'advance_payment',
            'remaining_payment',
            'payment_status',
        ]

        widgets = {

            'customer_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Customer Name'
                }
            ),

            'mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Mobile Number'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter Address'
                }
            ),

            'event': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'event_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            # timing માટેનું Widget (Morning / Evening selection)
            'timing': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # dholi (સંખ્યા વિકલ્પો) માટેનું Widget
            'dholi': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # Custom Dholi Count માટેનું Widget
            'custom_dholi_count': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter custom dhol count (if custom selected)'
                }
            ),

            'sound_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'custom_sound_count': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Custom Sound Count'
                }
            ),

            'advance_payment': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Advance Payment'
                }
            ),

            'remaining_payment': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Remaining Payment'
                }
            ),

            'payment_status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }