// Boolean - prawda / fa�sz

// Warto�ci boolean
let prawda = true;
let falsz = false;

console.log(prawda);
console.log(falsz);

// Por�wnania zwracaj� boolean
console.log(5 > 3);      // true
console.log(5 < 3);      // false
console.log(5 === 5);    // true
console.log(5 !== 3);    // true

// Operatory logiczne
console.log(true && true);    // true
console.log(true && false);   // false
console.log(true || false);   // true
console.log(!true);           // false

// Warunki zwracaj� boolean
let wiek = 18;
if (wiek >= 18) {
    console.log("Doros�y");
} else {
    console.log("Dziecko");
}
