from django.urls import path, include
from .views import liste_biens
from location_biens.views import home

urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
]

from .views import reserver_bien

urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
    path('biens/<int:bien_id>/reserver/', reserver_bien, name='reserver_bien'),
    path('biens/', include('location_biens.urls')),  # Remplacez 'votre_app' par le nom de votre application
    path('', home, name='home'),  # Utilisez la vue home
]
