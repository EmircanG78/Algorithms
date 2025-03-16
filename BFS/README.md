# 📚 BFS (Breadth First Search)

## 🚀 Açıklama
Genişlik öncelikli arama algoritmasıdır.  
Bir graf ya da ağaç üzerinde **katman katman** ilerleyerek, önce en yakın düğümleri ziyaret eder.  
👉 İlk giren, ilk çıkar (FIFO) mantığıyla çalışan bir **kuyruk (queue)** kullanılır.

---

## ✅ Temel Özellikler
- **Ziyaret edilen düğümleri sırayla işler.**
- **En kısa yol garantisi verir** (kenar maliyetleri eşitse).
- **FIFO kuyruğu kullanır** ve katman katman ilerler.

---

## 📌 Nasıl Çalışır?
1. Başlangıç düğümünü sıraya ekleriz.
2. Sıradaki düğümü çıkarır, ziyaret ederiz.
3. Ziyaret edilen düğümün **komşularını sıraya ekleriz.**
4. Sıra boşalana kadar devam ederiz.

---

## ✅ İyi Yönleri
- ✅ **En kısa yolu garantili bulur** (kenar maliyetleri eşitse).  
- ✅ **Adım sayısını minimize eder**: Çözüm bulunduğunda en kısa adım sayısıyla bulunur.  
- ✅ **Basit ve anlaşılırdır**, kolay uygulanır.  
- ✅ **Labirent çözümü**, **sosyal ağlarda bağlantı bulma**, **oyunlarda yapay zeka araması** gibi alanlarda çok kullanılır.  
- ✅ FIFO kuyruğu mantığı sayesinde **katman katman ilerler**, tüm olasılıkları sistematik olarak dener.

---

## ❌ Kötü Yönleri
- ❌ **Bellek kullanımı yüksektir**: Geniş veya karmaşık grafiklerde sırada çok fazla düğüm bekler.  
- ❌ **Kenar maliyetleri farklıysa** en kısa veya en ucuz yolu garanti etmez (bu durumda Dijkstra veya A* kullanılır).  
- ❌ **Derinliği fazla olan grafiklerde** yavaş olabilir, çünkü tüm katmanları sırayla gezer.  
- ❌ Gereksiz dallara dalabilir ve **zaman/memory** kaybı olabilir.

---

## 🎯 Ne Zaman Kullanılır?
- ✅ **Kenar maliyetleri eşitse**, en kısa yol bulunmak isteniyorsa.  
- ✅ **Bir noktadan başka bir noktaya ulaşılabilir mi?** sorusuna cevap aranıyorsa.  
- ✅ **Adım sayısını minimize etmek** gereken durumlarda (en kısa hamlede hedefe ulaşmak gibi).  
- ✅ **Labirent çözümü**, **yol bulma**, **sosyal ağ analizleri** gibi uygulamalarda.  
- ✅ **Oyunlarda veya yapay zeka aramalarında**, hedefe en hızlı ulaşmayı amaçlıyorsan.

---

## 🚫 Ne Zaman Kullanılmaz?
-  **Kenar maliyetleri farklıysa** ➡️ Dijkstra veya A* kullanılır.  
-  **Grafik çok büyükse** ve bellek sıkıntısı varsa ➡️ DFS veya özel arama algoritmaları tercih edilir.  
-  **Daha derin yollar daha önem arz ediyorsa** ➡️ DFS veya Iterative Deepening kullanılır.

---
