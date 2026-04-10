var ortanca = document.getElementById("ortanca-kardes");
console.log("Ortanca kardeş: ", ortanca);

var ebeveyn = ortanca.parentElement;
console.log("Ebeveyn: ", ebeveyn);

var öncekiKardes = ortanca.previousElementSibling;
console.log("Önceki kardeş: ", öncekiKardes);
var sonrakiKardes = ortanca.nextElementSibling;
console.log("Sonraki kardeş: ", sonrakiKardes);

öncekiKardes.classList.add("vurgulu");

var liste = document.getElementById("ebeveyn-liste");

console.log("Çocuklar: ", liste.children);
console.log("Çocuk sayısı: ", liste.childNodes);
console.log("ilk çocuk: ", liste.firstElementChild);
console.log("son çocuk: ", liste.lastElementChild);