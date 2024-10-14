from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Modèle pour les biens à louer
class Bien(models.Model):
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien vers le propriétaire (utilisateur)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='biens/', null=True, blank=True)  # Champ pour l'image
    est_publié = models.BooleanField(default=True)  # Champ pour gérer la publication
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)
    date_debut_disponibilite = models.DateField(null=True, blank=True)  
    date_fin_disponibilite = models.DateField(default="2024-01-01")


    def __str__(self):
        return self.titre

# Modèle pour les réservations
class Reservation(models.Model):
    locataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_as_locataire')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_as_utilisateur', default=1)  # Référence à l'utilisateur qui réserve
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    date_debut = models.DateField(null=False, blank=False)
    date_fin = models.DateField(null=False, blank=False)
    date_reservation = models.DateField(auto_now_add=True)  # Ajout de la date de réservation automatiquement
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    confirme = models.BooleanField(default=False)

    def clean(self):
        if self.date_fin < self.date_debut:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")

    def save(self, *args, **kwargs):
        if self.date_debut and self.date_fin:
            delta = (self.date_fin - self.date_debut).days
            self.montant_total = delta * self.bien.prix_par_jour
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Réservation de {self.locataire.username} pour {self.bien.titre}"

# Modèle pour les avis
class Avis(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='avis')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commentaire = models.TextField()

    def clean(self):
        if self.note < 1 or self.note > 5:
            raise ValidationError("La note doit être comprise entre 1 et 5.")

    def __str__(self):
        return f"Avis de {self.utilisateur.username} sur {self.bien.titre}"

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['bien', 'date_debut', 'date_fin', 'montant_total']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class ReservationForm(forms.Form):
    date_debut = forms.DateField(widget=forms.SelectDateWidget)
    date_fin = forms.DateField(widget=forms.SelectDateWidget)