var liste = document.getElementById("liste");
var yeniMadde = document.createElement("li");

yeniMadde.textContent = "Yumurta";
yeniMadde.classList.add("yeniEtiket");
liste.appendChild(yeniMadde);

var yeniMadde2 = document.createElement("li");

yeniMadde2.textContent = "Sıvı Yağ";
yeniMadde2.style.color = "brown";
yeniMadde2.style.fontSize = "20px";
yeniMadde2.style.backgroundColor = "gray";
liste.appendChild(yeniMadde2);

yeniMadde2.setAttribute("style", "color: aqua; font-size: 30px; background-color: orange;");