var tümürünler = document.querySelectorAll(".urun");

for (var urun of tümürünler) {
    var stokMiktarı = parseInt(urun.getAttribute("data-stok"));

    if(stokMiktarı == 0) {
        //ürün yoksa gizle
        urun.classList.add("gizle");
    } else {
        urun.classList.add("mevcut");
        console.log(urun.innerText, "stokta: ", stokMiktarı);
        urun.textContent += " (stokta: " + stokMiktarı + ")";
    }
}