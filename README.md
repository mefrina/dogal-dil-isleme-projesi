# Doğal Dil İşleme - Oyun Türleri 

Bu projede Steam oyun veri seti kullanılarak oyun türlerinin dağılımı analiz edilmiştir. İlk olarak genres sütunundaki veriler temizlenmiş, noktalı virgül yardımıyla oyun türlerine ayrılmış ve her oyunda tekrar eden türler kaldırılmıştır.

İlk analizde her oyun türünün kaç farklı oyunda bulunduğu hesaplanmış ve sonuçlar steam_game_genre_summary.csv dosyasına kaydedilmiştir.

İkinci analizde oyun türlerinin veri setindeki ayırt ediciliğini ve ağırlığını karşılaştırmak amacıyla TF-IDF yöntemi uygulanmıştır. Bu işlemde:

* TF (Term Frequency): Bir oyun türünün ilgili oyundaki görülme sayısının, o oyundaki toplam farklı tür sayısına bölünmesiyle hesaplanmıştır.
* IDF (Inverse Document Frequency): Toplam oyun sayısının, ilgili türün bulunduğu oyun sayısına bölünmesinin doğal logaritması alınarak hesaplanmıştır.
* TF-IDF: TF ve IDF değerleri çarpılarak her oyun için türlerin TF-IDF değerleri elde edilmiştir.

Son olarak her oyun türünün tüm oyunlar üzerindeki ortalama TF-IDF değeri hesaplanmıştır. Türün bulunmadığı oyunlar da ortalamaya sıfır değerleriyle dahil edilmiştir. 

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
