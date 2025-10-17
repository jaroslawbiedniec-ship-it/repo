// Tablice - kolekcja elementów

// Tworzenie tablicy
let owoce = ["jab³ko", "banana", "pomarañcza"];
console.log(owoce);

// Dostêp do elementu
console.log(owoce[0]); // jab³ko
console.log(owoce[1]); // banana

// Dodawanie elementu
owoce.push("gruszka");
console.log(owoce);

// Usuwanie ostatniego
owoce.pop();
console.log(owoce);

// D³ugoœæ tablicy
console.log(owoce.length);

// Iterowanie po tablicy
for (let owoc of owoce) {
    console.log(owoc);
}

// Metoda forEach
owoce.forEach((owoc, index) => {
    console.log(index, owoc);
});
