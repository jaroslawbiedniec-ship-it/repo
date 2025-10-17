// Event Listener - reagowanie na zdarzenia

// Klikniêcie
let przycisk = document.querySelector("button");
if (przycisk) {
    przycisk.addEventListener("click", () => {
        console.log("Klikniêto przycisk!");
    });
}

// Najechanie mysz¹
let element = document.querySelector(".element");
if (element) {
    element.addEventListener("mouseover", () => {
        console.log("Najechano mysz¹");
    });
}

// Opuszczenie mysz¹
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

// Wys³anie formularza
let forma = document.querySelector("form");
if (forma) {
    forma.addEventListener("submit", (event) => {
        event.preventDefault();
        console.log("Formularz wys³any");
    });
}

// Naciœniêcie klawisza
document.addEventListener("keypress", (event) => {
    console.log("Naciœniêty klawisz:", event.key);
});

// Zmiana rozmiaru okna
window.addEventListener("resize", () => {
    console.log("Zmieniono rozmiar okna");
});
