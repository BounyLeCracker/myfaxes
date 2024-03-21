from django.shortcuts import render, redirect
from .models import Cours, Sujet
from .forms import SujetForm

def accueil(request):
    cours = Cours.objects.all()
    return render(request, 'accueil.html', {'cours_list': cours})
    
# Affichage de la liste des sujets et des sujets
def liste_sujets(request):
    cours_code = request.GET.get('cours')
    if cours_code:
        sujets = Sujet.objects.filter(cours__code=cours_code)
    else:
        sujets = Sujet.objects.all()
    cours_list = Cours.objects.all()
    return render(request, 'liste_sujets.html', {'sujets': sujets, 'cours_list': cours_list})


def detail_sujet(request, sujet_id):
    sujet = Sujet.objects.get(id=sujet_id)
    return render(request, 'detail_sujet.html', {'sujet': sujet})


def ajouter_sujet(request):
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_sujets')
    else:
        form = SujetForm()
    return render(request, 'ajouter_sujet.html', {'form': form})
