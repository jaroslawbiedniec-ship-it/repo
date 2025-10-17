// API - pobieranie danych z internetu

// Fetch API - pobranie danych
fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log("B��d:", error));

// Async/Await z API
async function pobierzDane() {
    try {
        let response = await fetch("https://jsonplaceholder.typicode.com/users");
        let dane = await response.json();
        console.log(dane);
    } catch (error) {
        console.log("B��d:", error);
    }
}

pobierzDane();

// POST - wys�anie danych
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        title: "M�j post",
        body: "To jest tre�� posta",
        userId: 1
    })
})
.then(response => response.json())
.then(data => console.log("Odpowied�:", data))
.catch(error => console.log("B��d:", error));

// GET z parametrami
fetch("https://jsonplaceholder.typicode.com/posts?userId=1")
    .then(response => response.json())
    .then(posts => console.log("Posty u�ytkownika 1:", posts));
