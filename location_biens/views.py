from django.shortcuts import render, redirect, get_object_or_404
from .models import Bien  # Importation du modèle Bien
from .forms import ReservationForm  # Importation du formulaire de réservation
from django.utils import timezone
import logging
from django.contrib.auth.decorators import login_required  # Pour restreindre l'accès aux utilisateurs connectés
from django.contrib.auth import login
from .forms import SignUpForm
from datetime import timedelta  # Import pour calculer la différence entre deux dates

# Logger pour enregistrer les erreurs
logger = logging.getLogger(__name__)

# Page d'accueil
def home(request):
    return render(request, 'home.html')

# Liste des biens
def liste_biens(request):
    # Récupère tous les biens disponibles
    biens = Bien.objects.all()  
    return render(request, 'location_biens/liste_biens.html', {'biens': biens})

# Détails d'un bien spécifique
def bien_detail(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    return render(request, 'location_biens/bien_detail.html', {'bien': bien})

# Réserver un bien - réservé aux utilisateurs connectés
@login_required(login_url='login')  # Redirige les utilisateurs non authentifiés vers la page de connexion
def reserver_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.bien = bien
            reservation.locataire = request.user  # Associer l'utilisateur connecté à la réservation
            reservation.date_reservation = timezone.now()
            
            # Calcul du montant total en fonction des dates de début et de fin
            date_debut = reservation.date_debut
            date_fin = reservation.date_fin
            
            if date_debut and date_fin:
                # Calcul de la durée en jours
                duree = (date_fin - date_debut).days + 1  # +1 pour inclure la journée de début
                if duree > 0:
                    # Calcul du montant total en fonction du prix par jour
                    reservation.montant_total = duree * bien.prix_par_jour
                else:
                    form.add_error('date_fin', 'La date de fin doit être postérieure à la date de début.')
            else:
                form.add_error('date_debut', 'Veuillez entrer une date de début valide.')
                form.add_error('date_fin', 'Veuillez entrer une date de fin valide.')

            if not form.errors:  # S'il n'y a pas d'erreurs, enregistrer la réservation
                reservation.save()
                return redirect('reservation_succes')  # Remplacez par l'URL de redirection après réservation réussie
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = ReservationForm()

    return render(request, 'location_biens/reserver_bien.html', {'form': form, 'bien': bien})

# Inscription
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'location_biens/signup.html', {'form': form})
