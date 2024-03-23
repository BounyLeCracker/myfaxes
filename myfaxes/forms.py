from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Sujet, Filiere, Niveau, Etudiant

class ConnexionForm(AuthenticationForm):
    # On peut personnaliser votre formulaire de connexion ici si nécessaire
    pass

class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujet
        fields = ['cours', 'titre', 'type_sujet', 'annee', 'fichier']
        # On peut personnaliser la façon dont les champs sont affichés

class EtudiantRegistrationForm(UserCreationForm):
    cin = forms.CharField(max_length=8, required=True)
    date_naissance = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    lieu_naissance = forms.CharField(max_length=25, required=True)
    adresse = forms.CharField(max_length=75, required=True)
    telephone = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Etudiant
        fields = ('user', 'cin', 'date_naissance', 'lieu_naissance', 'adresse', 'telephone', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        etudiant = Etudiant.objects.create(user=user, cin=self.cleaned_data['cin'], date_naissance=self.cleaned_data['date_naissance'], lieu_naissance=self.cleaned_data['lieu_naissance'], adresse=self.cleaned_data['adresse'], telephone=self.cleaned_data['telephone'])
        return etudiant