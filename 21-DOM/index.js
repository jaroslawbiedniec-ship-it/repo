// DOM - Document Object Model

// Selekcja element�w
let element1 = document.getElementById("moje-id");
let element2 = document.querySelector(".klasa");
let element3 = document.querySelectorAll("p");

// Zmiana tekstu
let paragraf = document.querySelector("p");
if (paragraf) {
    paragraf.textContent = "Nowy tekst";
}

// Zmiana HTML
let div = document.getElementById("kontener");
if (div) {
    div.innerHTML = "<h1>Nag��wek</h1>";
}

// Zmiana atrybut�w
let link = document.querySelector("a");
if (link) {
    link.setAttribute("href", "https://example.com");
    link.textContent = "Kliknij mnie";
}

// Dodawanie/usuwanie klas
let przycisk = document.querySelector("button");
if (przycisk) {
    przycisk.classList.add("aktywny");
    przycisk.classList.remove("nieaktywny");
    przycisk.classList.toggle("zaznaczony");
}

// Zmiana styl�w
let box = document.querySelector(".box");
if (box) {
    box.style.backgroundColor = "red";
    box.style.padding = "20px";
    box.style.borderRadius = "10px";
}
