var kutu = document.getElementById("kutu");

document.getElementById("btnKirmizi").addEventListener("click", function() {
    kutu.style.backgroundColor = "red";
});

document.getElementById("btnYesil").addEventListener("click", function() {
    kutu.style.backgroundColor = "green";
});

document.getElementById("btnMavi").addEventListener("click", function() {
    kutu.style.backgroundColor = "blue";
});

document.getElementById("btnSifirla").addEventListener("click", function() {
    kutu.style.backgroundColor = "";
    kutu.style.width = "200px";
    kutu.style.height = "200px";
});

document.getElementById("btnBuyut").addEventListener("click", function() {
    kutu.style.width = "400px";
    kutu.style.height = "400px";
});