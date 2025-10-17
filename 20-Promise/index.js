// Promise - obiecanka asynchroniczna

// Tworzenie Promise
let promise = new Promise((resolve, reject) => {
    let sukces = true;
    
    if (sukces) {
        resolve("Operacja powiod³a siê!");
    } else {
        reject("Operacja siê nie powiod³a");
    }
});

// Then i catch
promise
    .then(wiadomoœæ => console.log(wiadomoœæ))
    .catch(b³¹d => console.log(b³¹d));

// Promise z opóŸnieniem
new Promise((resolve) => {
    setTimeout(() => {
        resolve("Gotowe po 2 sekundach");
    }, 2000);
})
.then(wynik => console.log(wynik));

// £añcuch Promise (Promise chain)
new Promise((resolve) => {
    resolve(10);
})
.then(liczba => {
    console.log("Liczba:", liczba);
    return liczba * 2;
})
.then(liczba => {
    console.log("Podwojona:", liczba);
    return liczba + 5;
})
.then(liczba => {
    console.log("Plus 5:", liczba);
});

// Promise.all - czekaj na wszystkie
Promise.all([
    Promise.resolve("Dane 1"),
    Promise.resolve("Dane 2"),
    Promise.resolve("Dane 3")
])
.then(dane => console.log(dane));
