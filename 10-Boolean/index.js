// Boolean - prawda / fa³sz

// Wartoœci boolean
let prawda = true;
let falsz = false;

console.log(prawda);
console.log(falsz);

// Porównania zwracaj¹ boolean
console.log(5 > 3);      // true
console.log(5 < 3);      // false
console.log(5 === 5);    // true
console.log(5 !== 3);    // true

// Operatory logiczne
console.log(true && true);    // true
console.log(true && false);   // false
console.log(true || false);   // true
console.log(!true);           // false

// Warunki zwracaj¹ boolean
let wiek = 18;
if (wiek >= 18) {
    console.log("Doros³y");
} else {
    console.log("Dziecko");
}
