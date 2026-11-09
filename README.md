# Doğal Dil İşleme - Oyun Türleri Analizi

Bu proje, Steam oyun veri setindeki oyun türlerinin dağılımını analiz eder. Veri setindeki `genres` sütunu incelenerek oyun türleri otomatik olarak tespit edilmiştir. İlk çıktı dosyasında her oyun türünün kaç oyunda bulunduğu hesaplanarak görülme sıklıkları belirlenmiştir. İkinci çıktı dosyasında ise TF-IDF yöntemiyle oyun türlerinin ortalama ağırlıkları hesaplanmıştır. Böylece oyun türleri hem görülme sıklıklarına hem de veri setindeki ayırt ediciliklerine göre karşılaştırılmıştır.

## Girdi

`data_set`: Analizde kullanılan Steam oyun veri seti (CSV formatı). Kod bu dosyadaki `genres` sütununu okuyarak oyun türlerini noktalı virgüle göre ayırır ve temizler.

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Regex

## Kullanılan Yöntem

- TF-IDF: Hazır bir TF-IDF kütüphanesi kullanılmadan NumPy ile hesaplanmıştır.

## Çıktılar

- `steam_game_genre_summary.csv`: Oyun türlerinin görülme sayıları.
- `steam_game_tfidf_summary.csv`: Oyun türlerinin ortalama TF-IDF değerleri.

Konsolda her iki analiz için ilk 10 sonuç gösterilir, CSV dosyalarında tüm sonuçlar saklanır.
