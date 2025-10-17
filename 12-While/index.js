// P�tla while

// Podstawowa p�tla while
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

// P�tla do...while (wykonuje si� minimum raz)
let x = 0;
do {
    console.log("Do while:", x);
    x++;
} while (x < 3);

// Break - wyj�cie z p�tli
let y = 0;
while (true) {
    if (y === 5) {
        break;
    }
    console.log(y);
    y++;
}

// Continue - pomi� iteracj�
let z = 0;
while (z < 5) {
    if (z === 2) {
        z++;
        continue;
    }
    console.log(z);
    z++;
}
