// Promise - obiecanka asynchroniczna

// Tworzenie Promise
let promise = new Promise((resolve, reject) => {
    let sukces = true;
    
    if (sukces) {
        resolve("Operacja powiod�a si�!");
    } else {
        reject("Operacja si� nie powiod�a");
    }
});

// Then i catch
promise
    .then(wiadomo�� => console.log(wiadomo��))
    .catch(b��d => console.log(b��d));

// Promise z op�nieniem
new Promise((resolve) => {
    setTimeout(() => {
        resolve("Gotowe po 2 sekundach");
    }, 2000);
})
.then(wynik => console.log(wynik));

// �a�cuch Promise (Promise chain)
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
