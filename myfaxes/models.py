from django.db import models

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.nom

class Sujet(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    type_sujet = models.CharField(max_length=50)  # TPE, CC, Examen
    annee = models.IntegerField()
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return f"{self.titre} ({self.type_sujet})"
