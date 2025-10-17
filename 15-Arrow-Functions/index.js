// Arrow Functions - funkcje strza�kowe

// Tradycyjna funkcja
function dodaj(a, b) {
    return a + b;
}
console.log(dodaj(5, 3));

// Arrow function - d�uga forma
const dodajArrow = (a, b) => {
    return a + b;
};
console.log(dodajArrow(5, 3));

// Arrow function - kr�tka forma (bez {} i return)
const odejmij = (a, b) => a - b;
console.log(odejmij(10, 3));

// Jeden parametr - bez nawias�w
const kwadrat = x => x * x;
console.log(kwadrat(5));

// Bez parametr�w
const powitanie = () => {
    return "Cze��!";
};
console.log(powitanie());

// Arrow functions z tablicami
let liczby = [1, 2, 3, 4, 5];

// Map - transformuj elementy
let podwojone = liczby.map(x => x * 2);
console.log(podwojone);

// Filter - odfiltruj elementy
let parzyste = liczby.filter(x => x % 2 === 0);
console.log(parzyste);
