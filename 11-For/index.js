// P�tla for

// Podstawowa p�tla for
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Liczenie od 1 do 10
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// Liczenie wstecz
for (let i = 10; i > 0; i--) {
    console.log(i);
}

// P�tla przez tablic�
let liczby = [1, 2, 3, 4, 5];
for (let i = 0; i < liczby.length; i++) {
    console.log(liczby[i]);
}

// For...of - nowoczesny spos�b
for (let liczba of liczby) {
    console.log(liczba);
}

// Zagnie�d�one p�tle
for (let i = 1; i <= 3; i++) {
    for (let j = 1; j <= 3; j++) {
        console.log(i=, j=);
    }
}
