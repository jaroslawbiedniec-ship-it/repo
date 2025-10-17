// Obiekty - kolekcja w³aœciwoœci

// Tworzenie obiektu
let osoba = {
    imie: "Jan",
    wiek: 25,
    miasto: "Warszawa"
};
console.log(osoba);

// Dostêp do w³aœciwoœci
console.log(osoba.imie);
console.log(osoba["wiek"]);

// Zmiana w³aœciwoœci
osoba.wiek = 26;
console.log(osoba);

// Dodanie nowej w³aœciwoœci
osoba.zawód = "Programista";
console.log(osoba);

// Metody w obiekcie
let samochód = {
    marka: "Toyota",
    model: "Corolla",
    jazda: function() {
        console.log("Jadê samochodem");
    }
};
samochód.jazda();
