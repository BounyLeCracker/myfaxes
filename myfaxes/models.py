from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm, CharField, PasswordInput, DateInput, EmailField, DateField
from django.core.exceptions import ValidationError


class Filiere(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Niveau(models.Model):
    NIVEAU_CHOICES = [
        ('Nineau 1', 'Nineau 1'),
        ('Nineau 2', 'Niveau 2'),
        ('Nineau 3', 'Niveau 3'),
    ]
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    nom = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    annee = models.IntegerField()

    class Meta:
        unique_together = ('filiere', 'nom', 'annee')
        verbose_name_plural = "niveaux"

    def __str__(self):
        return f"{self.nom}"

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cin = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$', 'Entrez un numéro CIN valide.')])
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=25)
    adresse = models.CharField(max_length=75)
    telephone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Entrez un numéro de téléphone valide.')])
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'cni'

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.cin}'

class Cours(models.Model):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, )
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.nom}"

class Sujet(models.Model):
    TYPE_SUJET_CHOICES = [
        ('TD', 'Travaux Dirigés'),
        ('TPE', 'Travaux Pratiques Encadrés'),
        ('CC', 'Contrôle Continu'),
        ('EXAM', 'Examen'),
    ]
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    type_sujet = models.CharField(max_length=4, choices=TYPE_SUJET_CHOICES)
    annee = models.IntegerField()
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return f"{self.titre} ({self.get_type_sujet_display()})"

class EtudiantRegistrationForm(UserCreationForm):
    cin = CharField(label='CIN', max_length=8)
    date_naissance = DateField(label='Date de naissance', widget=DateInput(attrs={'type': 'date'}))
    lieu_naissance = CharField(label='Lieu de naissance', max_length=25)
    adresse = CharField(label='Adresse', max_length=75)
    telephone = CharField(label='Téléphone', max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Entrez un numéro de téléphone valide.')])
    email = EmailField(label='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        etudiant = Etudiant.objects.create(
            user=user,
            cin=self.cleaned_data['cin'],
            date_naissance=self.cleaned_data['date_naissance'],
            lieu_naissance=self.cleaned_data['lieu_naissance'],
            adresse=self.cleaned_data['adresse'],
            telephone=self.cleaned_data['telephone'],
            email=self.cleaned_data['email']
        )
        return etudiant