from django.shortcuts import render, redirect, get_object_or_404
from .models import Bien, UserProfile, Reservation
from .forms import ReservationForm, SignUpForm, BienForm, UserProfileForm
from django.utils import timezone
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserUpdateForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirection vers le tableau de bord après la connexion
            return redirect('dashboard')  # 'dashboard' est le nom de l'URL vers ton tableau de bord
        else:
            # Si l'authentification échoue, on renvoie l'utilisateur sur la page de connexion
            return render(request, 'login.html', {'error': 'Nom d’utilisateur ou mot de passe incorrect.'})
    
    return render(request, 'login.html')

logger = logging.getLogger(__name__)

def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form})

@login_required
def dashboard_view(request):
    user_reservations = Reservation.objects.filter(locataire=request.user)
    user_biens = Bien.objects.filter(proprietaire=request.user)

    return render(request, 'dashboard.html', {
        'reservations': user_reservations,
        'biens': user_biens,
    })

def home(request):
    return render(request, 'home.html')

def liste_biens(request):
    biens = Bien.objects.all()
    biens = Bien.objects.all()
    for bien in biens:
        if not bien.image:
            # Attribuer une image par défaut si aucune image n'est associée
            bien.image = 'location_biens\Images\images_defaut.jpeg'  # Remplacez par le chemin d'une image par défaut
    return render(request, 'location_biens/liste_biens.html', {'biens': biens})
    
  

def bien_detail(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    return render(request, 'location_biens/bien_detail.html', {'bien': bien})

@login_required
def ajouter_bien(request):
    if request.method == "POST":
        form = BienForm(request.POST, request.FILES)
        if form.is_valid():
            bien = form.save(commit=False)
            bien.proprietaire = request.user  # Associer le bien à l'utilisateur connecté
            bien.save()
            return redirect('dashboard')  # Rediriger vers la liste des biens ou une autre vue valide
    else:
        form = BienForm()

    return render(request, 'location_biens/ajouter_bien.html', {'form': form})

@login_required(login_url='login')
def reserver_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.bien = bien
            reservation.locataire = request.user
            reservation.date_reservation = timezone.now()
            
            date_debut = reservation.date_debut
            date_fin = reservation.date_fin
            
            if date_debut and date_fin:
                duree = (date_fin - date_debut).days + 1
                if duree > 0:
                    reservation.montant_total = duree * bien.prix_par_jour
                else:
                    form.add_error('date_fin', 'La date de fin doit être postérieure à la date de début.')
            else:
                form.add_error('date_debut', 'Veuillez entrer une date de début valide.')
                form.add_error('date_fin', 'Veuillez entrer une date de fin valide.')

            if not form.errors:
                reservation.save()
                return redirect('reservation_succes')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = ReservationForm()

    return render(request, 'location_biens/reserver_bien.html', {'form': form, 'bien': bien})

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

def reservation_succes(request):
    return render(request, 'location_biens/reservation_succes.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Rediriger vers le tableau de bord après modification
    else:
        form = UserUpdateForm(instance=user)
    
    return render(request, 'location_biens/edit_profile.html', {'form': form})