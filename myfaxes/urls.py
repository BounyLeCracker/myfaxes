from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('sujets/', views.liste_sujets, name='liste_sujets'),
    path('sujets/<int:sujet_id>/', views.detail_sujet, name='detail_sujet'),
    path('ajouter/', views.ajouter_sujet, name='ajouter_sujet'),
] 
