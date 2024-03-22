from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

class Filiere(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Niveau(models.Model):
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    nom = models.CharField(max_length=10)
    annee = models.IntegerField()

    class Meta:
        unique_together = ('filiere', 'nom', 'annee')
        verbose_name_plural = "niveaux"

    def __str__(self):
        return f"{self.filiere.nom} - {self.nom} - {self.annee}"

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cin = models.CharField(max_length=8)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=25)
    adresse = models.CharField(max_length=75)
    telephone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', 'Entrez un numéro de téléphone valide.')])
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.cin}'

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.nom}"

class Sujet(models.Model):
    TYPE_SUJET_CHOICES = [
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
