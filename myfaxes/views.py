from django.contrib.auth import login
from .forms import ConnexionForm
from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cours, Sujet
from .forms import SujetForm


def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')  # Redirige vers la page d'accueil après la connexion
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', {'form': form})


def accueil(request):
    cours = Cours.objects.all()
    return render(request, 'accueil.html', {'cours_list': cours})

def liste_sujets(request):
    cours_code = request.GET.get('cours')
    if cours_code:
        sujets = Sujet.objects.filter(cours__code=cours_code).select_related('cours')
    else:
        sujets = Sujet.objects.all().select_related('cours')
    cours_list = Cours.objects.all()
    return render(request, 'liste_sujets.html', {'sujets': sujets, 'cours_list': cours_list})

def detail_sujet(request, sujet_id):
    try:
        sujet = get_object_or_404(Sujet, id=sujet_id)
    except Http404:
        return render(request, '404.html', status=404)
    return render(request, 'detail_sujet.html', {'sujet': sujet})

@login_required
def ajouter_sujet(request):
    if not request.user.has_perm('app.add_sujet'):
        raise PermissionDenied
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Ajouter un message de succès
            messages.success(request, 'Le sujet a été ajouté avec succès.')
            return redirect('liste_sujets')
    else:
        form = SujetForm()
    return render(request, 'ajouter_sujet.html', {'form': form})
