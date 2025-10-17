// Reduce - redukuj tablic� do jednej warto�ci

let liczby = [1, 2, 3, 4, 5];

// Suma wszystkich liczb
let suma = liczby.reduce((acc, x) => acc + x, 0);
console.log(suma); // 15

// Iloczyn wszystkich liczb
let iloczyn = liczby.reduce((acc, x) => acc * x, 1);
console.log(iloczyn); // 120

// Licznik element�w
let licznik = liczby.reduce((acc) => acc + 1, 0);
console.log(licznik); // 5

// Tablica obiekt�w - suma wiek�w
let osoby = [
    { imie: "Jan", wiek: 25 },
    { imie: "Maria", wiek: 30 },
    { imie: "Piotr", wiek: 28 }
];

let sumaWiek�w = osoby.reduce((acc, osoba) => acc + osoba.wiek, 0);
console.log(sumaWiek�w); // 83

// Grupowanie danych
let wyniki = [
    { przedmiot: "Matematyka", ocena: 4 },
    { przedmiot: "Polski", ocena: 5 },
    { przedmiot: "Matematyka", ocena: 3 }
];

let zgrupowane = wyniki.reduce((acc, item) => {
    if (!acc[item.przedmiot]) {
        acc[item.przedmiot] = [];
    }
    acc[item.przedmiot].push(item.ocena);
    return acc;
}, {});
console.log(zgrupowane);
