var icerikalan = document.getElementById("icerik-alanı");
var hedefkutu = document.getElementById("hedef-kutu");

console.log(icerikalan);
console.log(hedefkutu);
console.log("icerikalan id'sine sahip elementin içeriği: " + icerikalan.innerHTML);
console.log("hedefkutu id'sine sahip elementin içeriği: " + hedefkutu.innerHTML);

hedefkutu.innerHTML = "<p>Bu içerik <strong>JavaScript</strong> tarafından eklendi.</p>";
