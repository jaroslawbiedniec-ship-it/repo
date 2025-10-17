// Filter - filtrowanie tablicy

let liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Filtruj liczby parzyste
let parzyste = liczby.filter(x => x % 2 === 0);
console.log(parzyste); // [2, 4, 6, 8, 10]

// Filtruj liczby wi�ksze od 5
let wieksze = liczby.filter(x => x > 5);
console.log(wieksze); // [6, 7, 8, 9, 10]

// Tablica obiekt�w
let osoby = [
    { imie: "Jan", wiek: 25 },
    { imie: "Maria", wiek: 30 },
    { imie: "Piotr", wiek: 18 }
];

// Filtruj osoby doros�e
let doro�li = osoby.filter(osoba => osoba.wiek >= 18);
console.log(doro�li);

// Filtruj po imieniu
let wyszukane = osoby.filter(osoba => osoba.imie.includes("a"));
console.log(wyszukane);
