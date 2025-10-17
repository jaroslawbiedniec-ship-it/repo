// Map - transformacja tablicy

let liczby = [1, 2, 3, 4, 5];

// Pomnó¿ ka¿dy element przez 2
let podwojone = liczby.map(x => x * 2);
console.log(podwojone); // [2, 4, 6, 8, 10]

// Konwertuj liczby na stringi
let stringu = liczby.map(x => Liczba: \);
console.log(stringu);

// Tablica obiektów
let osoby = [
    { imie: "Jan", wiek: 25 },
    { imie: "Maria", wiek: 30 },
    { imie: "Piotr", wiek: 28 }
];

// Wyci¹gnij imiona
let imiona = osoby.map(osoba => osoba.imie);
console.log(imiona); // ["Jan", "Maria", "Piotr"]

// Zwiêksz wiek o 1
let zwiêkszonyWiek = osoby.map(osoba => ({
    ...osoba,
    wiek: osoba.wiek + 1
}));
console.log(zwiêkszonyWiek);
