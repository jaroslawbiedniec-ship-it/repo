// Try...Catch - obs�uga b��d�w

// Podstawowa struktura
try {
    let wynik = 10 / 2;
    console.log(wynik);
} catch (b��d) {
    console.log("Co� posz�o nie tak:", b��d);
}

// B��d w kodzie
try {
    let tablica = [1, 2, 3];
    console.log(tablica[0]);
    console.log(tablica[10]); // undefined, ale nie b��d
} catch (b��d) {
    console.log("B��d:", b��d);
}

// Finally - wykonuje si� zawsze
try {
    console.log("Spr�buj co�");
} catch (b��d) {
    console.log("B��d:", b��d);
} finally {
    console.log("To si� zawsze wykona");
}

// Throw - wyrzu� w�asny b��d
try {
    let wiek = -5;
    if (wiek < 0) {
        throw new Error("Wiek nie mo�e by� ujemny");
    }
} catch (b��d) {
    console.log("B��d:", b��d.message);
}
