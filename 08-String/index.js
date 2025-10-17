// String - tekst

// Tworzenie stringa
let tekst = "Cze�� �wiecie";
console.log(tekst);

// Concatenation - ��czenie string�w
let imie = "Jan";
let powitanie = "Cze�� " + imie;
console.log(powitanie);

// Template literals - bardziej czytelne
let wiek = 25;
console.log(Mam na imi�  i mam  lat);

// W�a�ciwo�ci i metody
console.log(tekst.length);           // D�ugo��
console.log(tekst.toUpperCase());    // Wielkie litery
console.log(tekst.toLowerCase());    // Ma�e litery
console.log(tekst.includes("�wiecie")); // Zawiera?
console.log(tekst.indexOf("�wiecie"));  // Indeks

// Podstring
console.log(tekst.substring(0, 6));  // "Cze�� "
