from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation, Bien, UserProfile

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['date_reservation']
        fields = ['date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ['titre', 'description', 'prix_par_jour', 'image']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'phone_number', 'address']
