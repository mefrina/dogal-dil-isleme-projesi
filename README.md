Doğal Dil İşleme Projesi – Steam Oyun Türleri Analizi

Bu proje, Steam oyunlarının tür dağılımını analiz ederek en sık karşılaşılan oyun türlerini belirler.
Ayrıca TF-IDF yöntemiyle oyun türlerinin veri setindeki ağırlıklarını hesaplar.
Temel amaç oyun türlerini metin işleme yöntemleriyle analiz etmek ve sonuçları karşılaştırılabilir hâle getirmektir.

Yapılan İşlemler

1. Steam veri seti Python ile yüklenir.
2. Eksik veriler ve gereksiz karakterler temizlenir.
3. Metinler küçük harfe dönüştürülür.
4. Oyun türleri noktalı virgüle göre ayrılır.
5. Tekrarlanan oyun türleri kaldırılır.
6. Her oyun türünün görülme sayısı hesaplanır.
7. Türler için bir sözlük (Vocabulary) oluşturulur.
8. TF matrisi hesaplanır.
9. IDF vektörü oluşturulur.
10. TF ve IDF değerleri çarpılarak TF-IDF matrisi elde edilir.
11. Ortalama TF-IDF değerleri hesaplanıp sıralanır.

Çıktılar

* steam_genre_summary.csv: Oyun türlerinin görülme sayıları.
* steam_tfidf_summary.csv: Oyun türlerinin ortalama TF-IDF değerleri.
