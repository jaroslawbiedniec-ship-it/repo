// Instrukcje warunkowe - if

let wiek = 18;

// Podstawowe if
if (wiek >= 18) {
    console.log("Jesteœ doros³y");
}

// if...else
if (wiek < 18) {
    console.log("Jesteœ dzieckiem");
} else {
    console.log("Jesteœ doros³y");
}

// if...else if...else
if (wiek < 13) {
    console.log("Jesteœ dzieckiem");
} else if (wiek < 18) {
    console.log("Jesteœ nastolatkiem");
} else {
    console.log("Jesteœ doros³y");
}
