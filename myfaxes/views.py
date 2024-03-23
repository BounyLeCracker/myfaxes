from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConnexionForm, SujetForm, EtudiantRegistrationForm
from .models import Cours, Sujet, Filiere, Niveau

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Vous êtes maintenant connecté.')
            return redirect('accueil')
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('accueil')


def accueil(request):
    # Récupérer toutes les filières, niveaux et cours pour les passer au template
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    cours = Cours.objects.all()
    return render(request, 'accueil.html', {
        'filiere_list': filieres,
        'niveau_list': niveaux,
        'cours_list': cours
    })

def liste_sujets(request):
    # Récupérer les paramètres du formulaire
    filiere_nom = request.GET.get('filiere')
    niveau_nom = request.GET.get('niveau')
    cours_code = request.GET.get('cours')

    # Filtrer les sujets en fonction des paramètres du formulaire
    if filiere_nom and niveau_nom and cours_code:
        sujets = Sujet.objects.filter(
            cours__code=cours_code,
            cours__niveau__filiere__nom=filiere_nom,
            cours__niveau__nom=niveau_nom
        ).select_related('cours')
    else:
        sujets = Sujet.objects.all().select_related('cours')

    cours_list = Cours.objects.all()
    return render(request, 'liste_sujets.html', {'sujets': sujets, 'cours_list': cours_list})

def detail_sujet(request, sujet_id):
    sujet = get_object_or_404(Sujet, id=sujet_id)
    return render(request, 'detail_sujet.html', {'sujet': sujet})

@login_required(login_url='connexion')
@permission_required('app.add_sujet', raise_exception=True)
def ajouter_sujet(request):
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            sujet = form.save(commit=False)
            sujet.utilisateur = request.user
            sujet.save()
            messages.success(request, 'Le sujet a été ajouté avec succès.')
            return redirect('liste_sujets')
    else:
        form = SujetForm()
    return render(request, 'ajouter_sujet.html', {'form': form})

def register_etudiant(request):
    if request.method == 'POST':
        form = EtudiantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.')
            return redirect('connexion')  # Redirigez vers la page de connexion
    else:
        form = EtudiantRegistrationForm()
    return render(request, 'register_etudiant.html', {'form': form})
