// Instrukcje warunkowe - if

let wiek = 18;

// Podstawowe if
if (wiek >= 18) {
    console.log("Jeste� doros�y");
}

// if...else
if (wiek < 18) {
    console.log("Jeste� dzieckiem");
} else {
    console.log("Jeste� doros�y");
}

// if...else if...else
if (wiek < 13) {
    console.log("Jeste� dzieckiem");
} else if (wiek < 18) {
    console.log("Jeste� nastolatkiem");
} else {
    console.log("Jeste� doros�y");
}
