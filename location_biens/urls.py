from django.urls import path
from .views import liste_biens, reserver_bien, home , bien_detail
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
    path('biens/<int:bien_id>/reserver/', reserver_bien, name='reserver_bien'),
    path('', home, name='home'),  # Utilisez la vue home pour la page d'accueil
    path('biens/<int:bien_id>/', bien_detail, name='bien_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='location_biens/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),

]
