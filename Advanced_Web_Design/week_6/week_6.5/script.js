var ekran = document.getElementById("ekran");

if (ekran) {
    ekran.tabIndex = 0;
    ekran.focus();
    ekran.addEventListener("keydown", function (event) {
        ekran.textContent = "Basılan Tuş: " + event.key;
    });
}

 