// JSON - format wymiany danych

// Obiekt JavaScript
let osoba = {
    imie: "Jan",
    wiek: 25,
    zawód: "Programista",
    aktywny: true
};

// Zamiana na JSON (stringified)
let jsonString = JSON.stringify(osoba);
console.log(jsonString);
// Output: {"imie":"Jan","wiek":25,"zawód":"Programista","aktywny":true}

// Zamiana JSON na obiekt
let jsonDane = '{"imie":"Maria","wiek":30}';
let parsedOsoba = JSON.parse(jsonDane);
console.log(parsedOsoba.imie); // Maria

// Tablica JSON
let osoby = [
    { imie: "Jan", wiek: 25 },
    { imie: "Maria", wiek: 30 },
    { imie: "Piotr", wiek: 28 }
];

let jsonOsoby = JSON.stringify(osoby);
console.log(jsonOsoby);

// Parsowanie tablicy JSON
let parsedOsoby = JSON.parse(jsonOsoby);
console.log(parsedOsoby[0].imie); // Jan

// Pretty print - formatowanie
let czytelnyJson = JSON.stringify(osoba, null, 2);
console.log(czytelnyJson);
