// Obiekty - kolekcja w�a�ciwo�ci

// Tworzenie obiektu
let osoba = {
    imie: "Jan",
    wiek: 25,
    miasto: "Warszawa"
};
console.log(osoba);

// Dost�p do w�a�ciwo�ci
console.log(osoba.imie);
console.log(osoba["wiek"]);

// Zmiana w�a�ciwo�ci
osoba.wiek = 26;
console.log(osoba);

// Dodanie nowej w�a�ciwo�ci
osoba.zaw�d = "Programista";
console.log(osoba);

// Metody w obiekcie
let samoch�d = {
    marka: "Toyota",
    model: "Corolla",
    jazda: function() {
        console.log("Jad� samochodem");
    }
};
samoch�d.jazda();
