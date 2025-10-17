// Funkcje - bloki kodu do ponownego u¿ycia

// Prosta funkcja
function powitanie() {
    console.log("Czeœæ!");
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

// Krótka forma arrow function
const kwadrat = x => x * x;
console.log(kwadrat(5));

// Funkcja zwracaj¹ca obiekt
function tworzyæOsobê(imie, wiek) {
    return { imie, wiek };
}
console.log(tworzyæOsobê("Jan", 30));
