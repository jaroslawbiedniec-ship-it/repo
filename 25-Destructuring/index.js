// Destructuring - rozpakowywanie danych

// Destructuring obiekt�w
let osoba = {
    imie: "Jan",
    wiek: 25,
    zaw�d: "Programista"
};

// Tradycyjnie
let imie1 = osoba.imie;
let wiek1 = osoba.wiek;

// Z destructuring
let { imie, wiek, zaw�d } = osoba;
console.log(imie, wiek, zaw�d);

// Destructuring z domy�lnymi warto�ciami
let { imie: nazwa = "Nieznane", miasto = "Warszawa" } = osoba;
console.log(nazwa, miasto);

// Destructuring tablic
let liczby = [1, 2, 3, 4, 5];

// Tradycyjnie
let pierwszy = liczby[0];
let drugi = liczby[1];

// Z destructuring
let [x, y, z] = liczby;
console.log(x, y, z);

// Destructuring z rest operatorem
let [a, b, ...reszta] = liczby;
console.log(a, b, reszta); // 1, 2, [3, 4, 5]

// Destructuring w funkcjach
function wyswietlOsob�({ imie, wiek }) {
    console.log(\\ ma \ lat\);
}

wyswietlOsob�({ imie: "Jan", wiek: 25 });

// Destructuring tablic w funkcjach
function suma([x, y]) {
    return x + y;
}
console.log(suma([5, 3])); // 8
