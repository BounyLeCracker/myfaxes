from django.contrib import admin
from .models import Filiere, Niveau, Cours, Sujet, Etudiant

admin.site.register(Filiere)
admin.site.register(Niveau)
admin.site.register(Cours)
admin.site.register(Sujet)
admin.site.register(Etudiant)
