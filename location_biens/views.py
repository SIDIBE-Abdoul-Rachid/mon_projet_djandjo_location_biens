from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Bien  # Assure-toi que Bien est bien importé
from .forms import ReservationForm  # Import du formulaire de réservation


from django.shortcuts import redirect
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def liste_biens(request):
    # Logique pour récupérer la liste des biens
    return render(request, 'location_biens/liste_biens.html')


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

