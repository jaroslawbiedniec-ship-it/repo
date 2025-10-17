// String - tekst

// Tworzenie stringa
let tekst = "Czeœæ Œwiecie";
console.log(tekst);

// Concatenation - ³¹czenie stringów
let imie = "Jan";
let powitanie = "Czeœæ " + imie;
console.log(powitanie);

// Template literals - bardziej czytelne
let wiek = 25;
console.log(Mam na imiê  i mam  lat);

// W³aœciwoœci i metody
console.log(tekst.length);           // D³ugoœæ
console.log(tekst.toUpperCase());    // Wielkie litery
console.log(tekst.toLowerCase());    // Ma³e litery
console.log(tekst.includes("Œwiecie")); // Zawiera?
console.log(tekst.indexOf("Œwiecie"));  // Indeks

// Podstring
console.log(tekst.substring(0, 6));  // "Czeœæ "
