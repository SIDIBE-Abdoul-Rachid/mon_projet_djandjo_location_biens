from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modèle pour les biens à louer
class Bien(models.Model):
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien vers le propriétaire (utilisateur)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# Modèle pour les réservations
class Reservation(models.Model):
    locataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_as_locataire')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations_as_utilisateur', default=1) # Référence à l'utilisateur qui réserve
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    confirme = models.BooleanField(default=False)
    date_reservation = models.DateTimeField(default=timezone.now)  # Valeur par défaut à maintenant
 

    def __str__(self):
        return f"Réservation de {self.locataire.username} pour {self.bien.titre}"

# Modèle pour les avis
class Avis(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='avis')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commentaire = models.TextField()

    def __str__(self):
        return f"Avis de {self.utilisateur.username} sur {self.bien.titre}"
