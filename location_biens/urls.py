from django.urls import path
from .views import liste_biens, reserver_bien, home , bien_detail

urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
    path('biens/<int:bien_id>/reserver/', reserver_bien, name='reserver_bien'),
    path('', home, name='home'),  # Utilisez la vue home pour la page d'accueil
    path('biens/<int:bien_id>/', bien_detail, name='bien_detail'),
]
