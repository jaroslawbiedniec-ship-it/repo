// Event Listener - reagowanie na zdarzenia

// Klikni�cie
let przycisk = document.querySelector("button");
if (przycisk) {
    przycisk.addEventListener("click", () => {
        console.log("Klikni�to przycisk!");
    });
}

// Najechanie mysz�
let element = document.querySelector(".element");
if (element) {
    element.addEventListener("mouseover", () => {
        console.log("Najechano mysz�");
    });
}

// Opuszczenie mysz�
if (element) {
    element.addEventListener("mouseout", () => {
        console.log("Opuszczono element");
    });
}

// Wpisanie tekstu
let input = document.querySelector("input");
if (input) {
    input.addEventListener("input", (event) => {
        console.log("Wpisany tekst:", event.target.value);
    });
}

// Wys�anie formularza
let forma = document.querySelector("form");
if (forma) {
    forma.addEventListener("submit", (event) => {
        event.preventDefault();
        console.log("Formularz wys�any");
    });
}

// Naci�ni�cie klawisza
document.addEventListener("keypress", (event) => {
    console.log("Naci�ni�ty klawisz:", event.key);
});

// Zmiana rozmiaru okna
window.addEventListener("resize", () => {
    console.log("Zmieniono rozmiar okna");
});
