# A* Algoritması (A-Star Algorithm)

## 📌 Genel Bakış
A* (A-Star) algoritması, en kısa yol bulma (pathfinding) ve grafik arama (graph traversal) problemlerinde kullanılan sezgisel (heuristic) bir algoritmadır. Haritalar üzerinde rota bulma, yapay zeka karakterlerinin hareket planlaması ve robotikte yol bulma gibi birçok alanda yaygın olarak kullanılır.

A* algoritması, Dijkstra Algoritması'nın güvenilirliğini ve Greedy Best-First Search yönteminin hızını bir araya getirir. **En kısa yolu bulur ve verimli çalışır.**

---

## 🧠 A* Algoritması Nasıl Çalışır?

A* algoritması, her adımda aşağıdaki maliyet fonksiyonunu minimize etmeye çalışır:

- f(n) = g(n) + h(n)

- `g(n)`: Başlangıç düğümünden `n` düğümüne kadar olan gerçek maliyet.
- `h(n)`: `n` düğümünden hedef düğüme olan tahmini (heuristic) maliyet.

### Adımlar
1. Başlangıç düğümünü açık listeye (open list) ekle.
2. Açık listedeki `f(n)` değeri en küçük olan düğümü seç.
3. Eğer bu düğüm hedefse, yolu tamamla ve sonlandır.
4. Aksi halde, komşu düğümleri değerlendir:
   - Her komşu için `g`, `h` ve `f` değerlerini hesapla.
   - Daha kısa bir yol bulunduysa, komşuyu açık listeye ekle veya güncelle.
5. 2. adıma dönerek işlemi tekrarla.

---

## ✅ Güçlü Yönleri
- **En kısa yolu garanti eder**, doğru heuristic kullanıldığında optimal çözüm üretir.
- **Hızlı ve etkilidir**, sezgisel yaklaşımı sayesinde gereksiz düğümlerden kaçınır.
- **Esnektir**, farklı `h(n)` fonksiyonları ile çeşitli problemlere uyarlanabilir.
- **Optimal ve tamdır**, yani çözüm varsa mutlaka bulur ve en iyi sonucu verir.

---

## ❌ Zayıf Yönleri
- **Bellek kullanımı yüksektir**: Büyük grafiklerde açık ve kapalı listeler çok fazla bellek tüketebilir.
- **Heuristic fonksiyona bağımlıdır**: Yanlış veya yetersiz heuristic, performansı ciddi şekilde düşürebilir.
- **Dinamik ortamlarda verimsiz olabilir**, çünkü çevre sürekli değişiyorsa algoritmanın yeniden çalıştırılması gerekebilir.
- **Yoğun bağlı grafiklerde** çok fazla düğüm üzerinde işlem yapması gerekebilir, bu da yavaşlamaya neden olur.

---

## 🎯 Ne Zaman Kullanılmalı?
- **Yol bulma problemlerinde**, örneğin harita tabanlı navigasyon sistemlerinde veya oyunlarda karakter hareketinde.
- **Durum uzayı büyük ama hedef net olduğunda**, yani başlangıç ve bitiş düğümleri belliyse.
- **Heuristic bilgi mevcutsa**, hedefe olan mesafeyi yaklaşık olarak tahmin edebiliyorsak.
- **Statik veya deterministik ortamlarda**, çünkü çevre sık sık değişmiyorsa performansı çok iyidir.

---

## 🚀 Uygulama Alanları
- **Oyun geliştirme**: NPC karakterlerinin rota planlaması (ör. Unity, Unreal Engine).
- **Robotik**: Engelleri aşarak hedefe güvenli bir şekilde varma.
- **Harita ve navigasyon uygulamaları**: Google Maps gibi platformlarda rota hesaplama.
- **Yapay zeka ve karar verme sistemleri**.

---

## 📂 Ek Kaynaklar
- [A* Pathfinding Explained Visually](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- "Artificial Intelligence: A Modern Approach" - Stuart Russell, Peter Norvig
- [Wikipedia - A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
