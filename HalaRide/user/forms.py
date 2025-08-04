from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):

    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )

    class Meta:
        model = Signup
        fields = ['email', 'password']


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )

    

class CarSearchForm(forms.Form):
    CAR_TYPE_CHOICES = [
    ('', '-- Choose Car Type --'),
    ('Sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('Hatchback', 'Hatchback'),
    ('MPV', 'MPV / Family Car'),
]

    SEATING_CHOICES = [
        ('', '-- Choose Seats --'),
        ('5', '5 Seats'),
        ('7', '7 Seats'),
       
    ]

    TRANSMISSION_CHOICES = [
        ('', '-- Choose Transmission --'),
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    car_type = forms.ChoiceField(
        choices=CAR_TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'car_type', 'name': 'car_type'})
    )

    seats = forms.ChoiceField(
        choices=SEATING_CHOICES,
        
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'seats', 'name': 'seats'})
    )

    transmission = forms.ChoiceField(
        choices=TRANSMISSION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'transmission', 'name': 'transmission'})
    )
