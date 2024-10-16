from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation, Bien, UserProfile, Avis
from .models import Review 



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['date_reservation']
        fields = ['date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ['titre', 'description', 'prix_par_jour', 'image']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'phone_number', 'address']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['note', 'commentaire']
    
    def clean_note(self):
        note = self.cleaned_data.get('note')
        if note < 1 or note > 5:
            raise forms.ValidationError("La note doit être comprise entre 1 et 5.")
        return note

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']