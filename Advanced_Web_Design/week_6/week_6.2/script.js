var button = document.getElementById("btn");
button.onclick = function() {
    alert("Merhaba Onclick");
}

button.addEventListener("click", function() {
    alert("Merhaba EventListener");
});