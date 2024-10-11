from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Bien  # Assure-toi que Bien est bien défini dans models.py
from .forms import ReservationForm  # Import du formulaire de réservation
from django.utils import timezone
import logging
from django.contrib.auth.decorators import login_required  # Pour restreindre l'accès aux utilisateurs connectés
from django.contrib.auth import login
from .forms import SignUpForm

# Home page
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
            reservation.save()
            return redirect('success_url')  # Remplacez par l'URL de redirection après réservation réussie
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = ReservationForm()

    return render(request, 'location_biens/reserver_bien.html', {'form': form, 'bien': bien})

# Logger pour enregistrer les erreurs
logger = logging.getLogger(__name__)

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