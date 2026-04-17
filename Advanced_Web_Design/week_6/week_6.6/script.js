var metin = document.getElementById("metin");
var sayac = document.getElementById("sayac");


if (metin && sayac) {
    var MAX_CHARS = 250;

    metin.addEventListener("input", function (e) {
        var val = e.target.value;
        if (val.length > MAX_CHARS) {
            e.target.value = val.slice(0, MAX_CHARS);
            val = e.target.value;
        }

        var karakterSayisi = val.length;
        sayac.textContent = karakterSayisi;

        if (karakterSayisi >= 200) {
            metin.style.color = "red";
        } else if (karakterSayisi >= 150) {
            metin.style.color = "orange";
        } else if (karakterSayisi >= 100) {
            metin.style.color = "green";
        } else {
            metin.style.color = "";
        }
    });
}

    