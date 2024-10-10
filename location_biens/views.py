from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Bien  # Assure-toi que Bien est bien défini dans models.py
from .forms import ReservationForm  # Import du formulaire de réservation

def home(request):
    return render(request, 'home.html')

def liste_biens(request):
    # Logique pour récupérer la liste des biens
    biens = Bien.objects.all()  # Récupère tous les biens disponibles
    return render(request, 'location_biens/liste_biens.html', {'biens': biens})

def bien_detail(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    return render(request, 'location_biens/bien_detail.html', {'bien': bien})

def reserver_bien(request, bien_id):
    bien = Bien.objects.get(id=bien_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.bien = bien
            reservation.save()
            return redirect('liste_biens')
    else:
        form = ReservationForm()
    return render(request, 'location_biens/reserver_bien.html', {'form': form, 'bien': bien})
