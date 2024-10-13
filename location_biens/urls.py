from django.urls import path
from .views import liste_biens, reserver_bien, home , bien_detail
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ajouter_bien
from .views import reserver_bien, reservation_succes
from .views import edit_profile


urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
    path('biens/<int:bien_id>/reserver/', reserver_bien, name='reserver_bien'),
    path('', home, name='home'),
    path('biens/<int:bien_id>/', bien_detail, name='bien_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='location_biens/login.html', redirect_authenticated_user=True, next_page='dashboard'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ajouter/', ajouter_bien, name='ajouter_bien'),  # Ajoutez cette ligne
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('reservation/succes/', reservation_succes, name='reservation_succes'),
    path('edit-profile/', edit_profile, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
