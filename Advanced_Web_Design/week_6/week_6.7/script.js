var girdi = document.getElementById("girdi");
var ekleBtn = document.getElementById("ekleBtn");
var liste = document.getElementById("liste");
var silBtn = document.getElementById("silBtn");
var toplamSayac = document.getElementById("toplamSayac");
var tamamlandiSayac = document.getElementById("tamamlandiSayac");


function gorevEkle() {
    var yeniGorev = girdi.value.trim();
    if (yeniGorev) {
            var li = document.createElement("li");

            var span = document.createElement("span");
            span.className = "gorev-text";
            span.textContent = yeniGorev;

            var delBtn = document.createElement("button");
            delBtn.className = "delete-btn";
            delBtn.type = "button";
            delBtn.textContent = "Sil";

            delBtn.addEventListener("click", function (e) {
                e.stopPropagation();
                if (li.parentNode) {
                    li.parentNode.removeChild(li);
                    updateCounters();
                }
            });

            li.addEventListener("click", function () {
                li.classList.toggle("tamamlandi");
                updateCounters();
            });

            li.appendChild(span);
            li.appendChild(delBtn);
            liste.appendChild(li);
            girdi.value = "";
            ekleBtn.disabled = true;
            updateCounters();
    }
}


if (ekleBtn && girdi && liste) {
    ekleBtn.addEventListener("click", function () {
        gorevEkle();
    });

    function updateEkleState() {
        ekleBtn.disabled = !girdi.value.trim();
    }

    girdi.addEventListener("input", updateEkleState);
    updateEkleState();

    girdi.addEventListener("keypress", function (e) {
        if (e.key === "Enter" && girdi.value.trim()) {
            gorevEkle();
        }
    });
}


if (silBtn && liste) {
    silBtn.addEventListener("click", function () {
        liste.innerHTML = "";
        updateCounters();
    });
}



var tamamlandiSayac = document.getElementById("tamamlandiSayac");

function guncelleTamamlandiSayac() {
    var tamamlandiGorevler = document.querySelectorAll("#liste li.tamamlandi");
    if (tamamlandiSayac) {
        tamamlandiSayac.textContent = tamamlandiGorevler.length;
    }
}

function updateCounters() {
    if (toplamSayac) {
        toplamSayac.textContent = liste.querySelectorAll('li').length;
    }
    if (tamamlandiSayac) {
        tamamlandiSayac.textContent = document.querySelectorAll('#liste li.tamamlandi').length;
    }
}

