// Çok basit ve açıklayıcı örnekler — yeni başlayanlar için
// Bu dosya sayfanın sonunda çağrıldığı için elementler hazırdır.

var baslik = document.getElementById('title');
var aciklama = document.querySelector('.description');
var girdi = document.getElementById('itemInput');
var ekleBtn = document.getElementById('addBtn');
var temizleBtn = document.getElementById('clearBtn');
var liste = document.getElementById('itemsList');
var logEl = document.getElementById('log');

// Başlık ve açıklama -> ekrana yazı koyma
baslik.textContent = 'Basit DOM Örnekleri';
aciklama.textContent = 'Aşağıya öğe ekleyin ve tıklayın.';

// Başlangıçta bazı öğeler ekleyelim (manuel olarak)
var ilk1 = document.createElement('li'); ilk1.textContent = 'Alpha'; liste.appendChild(ilk1);
var ilk2 = document.createElement('li'); ilk2.textContent = 'Beta'; liste.appendChild(ilk2);
var ilk3 = document.createElement('li'); ilk3.textContent = 'Gamma'; liste.appendChild(ilk3);

// Basit döngü ile tüm li öğelerinin yazı boyutunu ayarla
var tumleri = document.getElementsByTagName('li');
for (var i = 0; i < tumleri.length; i++) {
  tumleri[i].style.fontSize = '14px';
}

// -----------------------------
// Parent / Child / Sibling örnekleri
// Yeni başlayanlar için temel gezinme komutları gösteriliyor
// - parentNode / parentElement: ebeveyn öğeyi alır
// - children / firstElementChild / lastElementChild: çocuk öğeler
// - nextElementSibling / previousElementSibling: kardeş öğeler
// -----------------------------

// İlk li öğesini al
var ilkLi = tumleri[0];
// Ebeveyn düğümünü al (bu durumda <ul>)
var ebeveyn = ilkLi.parentNode;
if (ebeveyn) {
  // Görsel olarak vurgulamak için arka plan ekle
  ebeveyn.style.backgroundColor = '#fff8db';
  logEl.textContent = 'Ebeveyn vurgulandı.';
}

// Ebeveynin çocuklarını (HTMLCollection) al ve sayısını göster
var cocuklar = ebeveyn.children; // sadece element düğümleri
if (cocuklar) {
  logEl.textContent = logEl.textContent + ' Çocuk sayısı: ' + cocuklar.length;
}

// İlk ve son çocuklara basit stil ver
if (ebeveyn.firstElementChild) {
  ebeveyn.firstElementChild.style.fontWeight = '700';
}
if (ebeveyn.lastElementChild) {
  ebeveyn.lastElementChild.style.opacity = '0.8';
}

// Kardeş öğelere erişim: nextElementSibling ve previousElementSibling
var sonraki = ilkLi.nextElementSibling; // ilk sonrasındaki öğe
if (sonraki) {
  sonraki.style.color = 'blue';
}
var onceki = ilkLi.previousElementSibling; // ilk öncesindeki öğe (genelde yok)
if (onceki) {
  onceki.style.color = 'green';
}

// İlk çocuk (liste içindeki ilk öğe) üzerinde küçük bir çerçeve göster
var ilkCocuk = liste.firstElementChild;
if (ilkCocuk) {
  ilkCocuk.style.border = '1px solid #ddd';
}

// Ekle butonuna basit davranış: input içeriğini listeye ekle
ekleBtn.onclick = function () {
  var deger = girdi.value;
  if (!deger) {
    logEl.textContent = 'Lütfen bir metin girin.';
    return;
  }
  var li = document.createElement('li');
  li.textContent = deger;
  // Basit: tıklanınca üstünü çiz (toggle)
  li.onclick = function () {
    if (this.style.textDecoration === 'line-through') {
      this.style.textDecoration = '';
    } else {
      this.style.textDecoration = 'line-through';
    }
  };
  liste.appendChild(li);
  girdi.value = '';
  logEl.textContent = 'Öğe eklendi.';
};

// Temizle butonu: tüm öğeleri kaldır
temizleBtn.onclick = function () {
  while (liste.firstChild) {
    liste.removeChild(liste.firstChild);
  }
  logEl.textContent = 'Liste temizlendi.';
};

// -----------------------------
// addEventListener vs onclick örneği
// - onclick: aynı özellik yeniden atanırsa önceki silinir (sadece son atama geçerlidir)
// - addEventListener: birden çok dinleyici eklenebilir; hepsi çalışır
// Basit ve görsel bir karşılaştırma ekleyelim.
// -----------------------------

var karsilastirma = document.createElement('div');
var aciklama = document.createElement('p');
aciklama.textContent = 'addEventListener vs onclick karşılaştırması:';
karsilastirma.appendChild(aciklama);

// onclick örneği (son atama geçerli olur)
var butonOnclick = document.createElement('button');
butonOnclick.textContent = 'onclick örneği';
// İlk atama
butonOnclick.onclick = function () { logEl.textContent = 'onclick: birinci handler çalıştı'; };
// İkinci atama -> birinci ata silinir, sadece bu çalışır
butonOnclick.onclick = function () { logEl.textContent = 'onclick: ikinci handler (birinci silindi)'; };
karsilastirma.appendChild(butonOnclick);

// addEventListener örneği (birden fazla çalışır)
var butonAdd = document.createElement('button');
butonAdd.textContent = 'addEventListener örneği';
butonAdd.addEventListener('click', function () { logEl.textContent = 'addEventListener: birinci handler çalıştı'; });
butonAdd.addEventListener('click', function () { logEl.textContent = 'addEventListener: ikinci handler çalıştı (her ikisi de çalışır)'; });
karsilastirma.appendChild(butonAdd);

// Karşılaştırma bölümünü sayfaya ekles
var ana = document.querySelector('main') || document.body;
ana.appendChild(karsilastirma);

