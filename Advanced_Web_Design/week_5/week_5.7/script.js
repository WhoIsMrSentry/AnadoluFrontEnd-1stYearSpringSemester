var ogrenciler = [
    { isim: "Cafer Ege Ejder", not: 75 },
    { isim: "Ekrem Tezcan Sarıdağ", not: 20 },
    { isim: "Mihriban Üçkuyulu", not: 85 },
    { isim: "Mustafa Cumhur Özkaya", not: 50 }
];

var listeKapsayici = document.getElementById("sonucListe");

for (var i = 0; i < ogrenciler.length; i++) {
    var ogrenci = ogrenciler[i];

    var kart = document.createElement("p");
    kart.classList.add("ogrencikarti");
    kart.textContent = ogrenci.isim + " - Not: " + ogrenci.not;
    listeKapsayici.appendChild(kart);

}


//listeden 50 üstü alanlar başarılı yeiş yansın 50 altı alanlar başarısız kırmızı yansın

var kartlar = document.getElementsByClassName("ogrencikarti");

for (var j = 0; j < kartlar.length; j++) {
    var kart = kartlar[j];
    var not = parseInt(kart.textContent.split(" - Not: ")[1]);

    if (not >= 50) {
        kart.classList.add("basarili");
    } else {
        kart.classList.add("basarisiz");
    }
}
