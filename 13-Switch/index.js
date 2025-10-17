// Switch - warunki dla wielu wartoœci

let dzieñ = 3;

switch (dzieñ) {
    case 1:
        console.log("Poniedzia³ek");
        break;
    case 2:
        console.log("Wtorek");
        break;
    case 3:
        console.log("Œroda");
        break;
    case 4:
        console.log("Czwartek");
        break;
    case 5:
        console.log("Pi¹tek");
        break;
    default:
        console.log("Weekend");
}

// Switch z stringami
let owoc = "jab³ko";

switch (owoc) {
    case "jab³ko":
        console.log("To jab³ko");
        break;
    case "banana":
        console.log("To banana");
        break;
    default:
        console.log("Nieznany owoc");
}
