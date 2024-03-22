from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('sujets/', views.liste_sujets, name='liste_sujets'),
    path('sujets/<int:sujet_id>/', views.detail_sujet, name='detail_sujet'),
    path('ajouter/', views.ajouter_sujet, name='ajouter_sujet'),
    path('inscription/', views.register_etudiant, name='register_etudiant'),
    path('connexion/', views.connexion, name='connexion'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('deconnexion/', views.custom_logout, name='custom_logout'),
] 

