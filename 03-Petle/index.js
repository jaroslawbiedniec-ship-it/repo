// Pêtle - powtarzanie kodu

// Pêtla for
for (let i = 0; i < 5; i++) {
    console.log("Powtórzenie:", i);
}

// Pêtla while
let licznik = 0;
while (licznik < 3) {
    console.log("While:", licznik);
    licznik++;
}

// Break - wyjœcie z pêtli
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// Continue - pomiñ iteracjê
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        continue;
    }
    console.log(i);
}
