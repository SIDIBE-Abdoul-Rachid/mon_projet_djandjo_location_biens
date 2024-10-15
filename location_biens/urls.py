from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    ajouter_bien,
    ajouter_avis,
    bien_detail,
    dashboard_view,
    edit_profile,
    home,
    liste_biens,
    modifier_avis,
    reservation_succes,
    reserver_bien,
    supprimer_avis,
    signup,
)

urlpatterns = [
    path('biens/', liste_biens, name='liste_biens'),
    path('biens/<int:bien_id>/reserver/', reserver_bien, name='reserver_bien'),
    path('', home, name='home'),
    path('biens/<int:bien_id>/', bien_detail, name='bien_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='location_biens/login.html', redirect_authenticated_user=True, next_page='dashboard'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', signup, name='signup'),
    path('ajouter/', ajouter_bien, name='ajouter_bien'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('reservation/succes/', reservation_succes, name='reservation_succes'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('bien/<int:bien_id>/ajouter-avis/', ajouter_avis, name='ajouter_avis'),
    path('avis/modifier/<int:avis_id>/', modifier_avis, name='modifier_avis'),
    path('avis/supprimer/<int:avis_id>/', supprimer_avis, name='supprimer_avis'),
    path('contacts/', views.contacts, name='contacts'),
    path('reserver-bien-paypal/<int:bien_id>/', views.reserver_bien_paypal, name='reserver_bien_paypal'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('reservation-cancel/', views.reservation_cancel, name='reservation_cancel'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
