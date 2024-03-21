// Sélectionnez l'icône du menu hamburger et le menu
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

// Fonction pour basculer la classe 'active' sur le menu
function toggleMenu() {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
}

// Écouteur d'événement pour le clic sur l'icône du menu hamburger
hamburger.addEventListener('click', toggleMenu);
