var buton = document.getElementById("btngoster");
var buton2 = document.getElementById("btngizle");

var mesaj = document.getElementById("mesaj");

buton.addEventListener("click", function () {
    mesaj.textContent = "Mesaj gizlendi.";
});


buton2.addEventListener("click", function () {
    mesaj.textContent = "...";
});