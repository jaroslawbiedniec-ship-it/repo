// Funkcje - bloki kodu do ponownego u�ycia

// Prosta funkcja
function powitanie() {
    console.log("Cze��!");
}
powitanie();

// Funkcja z parametrami
function dodaj(a, b) {
    return a + b;
}
console.log(dodaj(5, 3));

// Arrow function
const mnoz = (x, y) => {
    return x * y;
};
console.log(mnoz(4, 5));

// Kr�tka forma arrow function
const kwadrat = x => x * x;
console.log(kwadrat(5));

// Funkcja zwracaj�ca obiekt
function tworzy�Osob�(imie, wiek) {
    return { imie, wiek };
}
console.log(tworzy�Osob�("Jan", 30));
