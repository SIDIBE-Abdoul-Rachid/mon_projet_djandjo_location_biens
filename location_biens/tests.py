from django.shortcuts import render
from .models import Bien

def liste_biens(request):
    biens = Bien.objects.all()
    return render(request, 'location_biens/liste_biens.html', {'biens': biens})
