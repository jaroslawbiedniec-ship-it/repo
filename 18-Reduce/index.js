// Reduce - redukuj tablicê do jednej wartoœci

let liczby = [1, 2, 3, 4, 5];

// Suma wszystkich liczb
let suma = liczby.reduce((acc, x) => acc + x, 0);
console.log(suma); // 15

// Iloczyn wszystkich liczb
let iloczyn = liczby.reduce((acc, x) => acc * x, 1);
console.log(iloczyn); // 120

// Licznik elementów
let licznik = liczby.reduce((acc) => acc + 1, 0);
console.log(licznik); // 5

// Tablica obiektów - suma wieków
let osoby = [
    { imie: "Jan", wiek: 25 },
    { imie: "Maria", wiek: 30 },
    { imie: "Piotr", wiek: 28 }
];

let sumaWieków = osoby.reduce((acc, osoba) => acc + osoba.wiek, 0);
console.log(sumaWieków); // 83

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
