// Try...Catch - obs³uga b³êdów

// Podstawowa struktura
try {
    let wynik = 10 / 2;
    console.log(wynik);
} catch (b³¹d) {
    console.log("Coœ posz³o nie tak:", b³¹d);
}

// B³¹d w kodzie
try {
    let tablica = [1, 2, 3];
    console.log(tablica[0]);
    console.log(tablica[10]); // undefined, ale nie b³¹d
} catch (b³¹d) {
    console.log("B³¹d:", b³¹d);
}

// Finally - wykonuje siê zawsze
try {
    console.log("Spróbuj coœ");
} catch (b³¹d) {
    console.log("B³¹d:", b³¹d);
} finally {
    console.log("To siê zawsze wykona");
}

// Throw - wyrzuæ w³asny b³¹d
try {
    let wiek = -5;
    if (wiek < 0) {
        throw new Error("Wiek nie mo¿e byæ ujemny");
    }
} catch (b³¹d) {
    console.log("B³¹d:", b³¹d.message);
}
