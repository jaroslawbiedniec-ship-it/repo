// P�tle - powtarzanie kodu

// P�tla for
for (let i = 0; i < 5; i++) {
    console.log("Powt�rzenie:", i);
}

// P�tla while
let licznik = 0;
while (licznik < 3) {
    console.log("While:", licznik);
    licznik++;
}

// Break - wyj�cie z p�tli
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// Continue - pomi� iteracj�
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        continue;
    }
    console.log(i);
}
