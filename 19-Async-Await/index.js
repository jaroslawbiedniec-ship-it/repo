// Async/Await - asynchroniczny kod

// Async funkcja zwraca Promise
async function pobranie() {
    console.log("Zaczynam pobieranie...");
    
    // Czekaj 2 sekundy
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    console.log("Dane pobrane!");
    return "Dane z serwera";
}

pobranie().then(dane => {
    console.log(dane);
});

// Try...Catch z async/await
async function pobierzDane() {
    try {
        console.log("Pobieranie...");
        // Symulacja opóŸnienia
        await new Promise(resolve => setTimeout(resolve, 1000));
        console.log("Gotowe!");
    } catch (b³¹d) {
        console.log("B³¹d:", b³¹d);
    }
}

pobierzDane();

// Wielokrotne awaity
async function wieleOperacji() {
    console.log("Start");
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log("Po 1 sekundzie");
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log("Po 2 sekundach");
}

wieleOperacji();
