from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Sujet

class ConnexionForm(AuthenticationForm):
    # Vous pouvez ajouter des personnalisations ici si nécessaire
    pass

class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujet
        fields = ['cours', 'titre', 'type_sujet', 'annee', 'fichier']
