// JavaScript
// Sélectionner le menu hamburger, le menu de navigation et les liens du menu
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const navLinks = document.querySelectorAll(".nav-link");

// Ajouter un écouteur d'événement au clic sur chaque lien du menu
navLinks.forEach((navLink) => {
  navLink.addEventListener("click", () => {
    // Désactiver l'élément input
    document.getElementById("toggle").checked = false;
    // Fermer le menu responsive
    showResponsiveMenu();
  });
});

// Définir la fonction qui affiche ou masque le menu responsive
function showResponsiveMenu() {
  var menu = document.getElementById("topnav_responsive_menu");
  var icon = document.getElementById("topnav_hamburger_icon");
  var root = document.getElementById("root");
  if (menu.className === "") {
    menu.className = "open";
    icon.className = "open";
    root.style.overflowY = "hidden";
  } else {
    menu.className = "";
    icon.className = "";
    root.style.overflowY = "";
  }
} // Ajouter une parenthèse fermante ici
