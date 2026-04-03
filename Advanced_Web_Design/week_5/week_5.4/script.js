var resim = document.getElementById("resim");
console.log("Resim elementinin kaynağı", resim.getAttribute("src"));
console.log("Resim elemetinin kaynağı: ", resim.src);
console.log("Resim elemetinin genişliği: ", resim.width);
console.log("Resim elemetinin yüksekliği: ", resim.height);
console.log("Resim elemetinin alternatif metni: ", resim.alt);

resim.setAttribute("alt", "Sentry Old Logo replaced");
resim.setAttribute("width", "1366");
resim.setAttribute("height", "768");

removeAttribute("width");

var resim2 = document.getElementById("resim2");
console.log("Resim 2 elemetinin kaynağı: ", resim2.src);


resim2.setAttribute("alt", "Sentry Old Logo2");
resim2.setAttribute("width", "720");
resim2.setAttribute("height", "450");

metin.classList.add("kalin");
metin.classList.add("italic");
metin.classList.add("renkkirmizi");
metin.remove("italic");
metin.toggle("italic");
metin.classList.toggle("italic")
