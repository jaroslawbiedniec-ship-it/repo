// Tablice - kolekcja element�w

// Tworzenie tablicy
let owoce = ["jab�ko", "banana", "pomara�cza"];
console.log(owoce);

// Dost�p do elementu
console.log(owoce[0]); // jab�ko
console.log(owoce[1]); // banana

// Dodawanie elementu
owoce.push("gruszka");
console.log(owoce);

// Usuwanie ostatniego
owoce.pop();
console.log(owoce);

// D�ugo�� tablicy
console.log(owoce.length);

// Iterowanie po tablicy
for (let owoc of owoce) {
    console.log(owoc);
}

// Metoda forEach
owoce.forEach((owoc, index) => {
    console.log(index, owoc);
});
