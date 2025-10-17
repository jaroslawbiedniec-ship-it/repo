// Pêtla while

// Podstawowa pêtla while
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// Liczenie od 1 do 10
let licznik = 1;
while (licznik <= 10) {
    console.log(licznik);
    licznik++;
}

// Pêtla do...while (wykonuje siê minimum raz)
let x = 0;
do {
    console.log("Do while:", x);
    x++;
} while (x < 3);

// Break - wyjœcie z pêtli
let y = 0;
while (true) {
    if (y === 5) {
        break;
    }
    console.log(y);
    y++;
}

// Continue - pomiñ iteracjê
let z = 0;
while (z < 5) {
    if (z === 2) {
        z++;
        continue;
    }
    console.log(z);
    z++;
}
