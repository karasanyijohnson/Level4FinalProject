from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Phone number'}))
    # check_in = forms.CharField(widget=forms.TextInput())
    # check_out = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Booking
        fields = ('firstName','lastName', 'email', 'phoneNumber','check_in','check_out')
        widgets = {
            'check_in': DateInput(),
            'check_out': DateInput()
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']