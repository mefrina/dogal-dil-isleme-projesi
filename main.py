import re
import pandas as pd
import numpy as np




def clean_text(text):
    if type(text) != str:
        return ""

    text = text.replace("Â", "a").replace("â", "a")
    text = text.replace("î", "i").replace("Î", "i")
    text = text.replace("İ", "i")
    text = text.replace("I", "ı")

    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^A-Za-z0-9;âîığüşöçİĞÜŞÖÇ]+", " ", text)

    return " ".join(text.lower().strip().split())


def main():
    print("[+] Loading dataset...")
    df = pd.read_csv("data_set")
    print(f"[+] Total games: {len(df)}")

    if "genres" not in df.columns:
        print("[-] genres column not found!")
        return

    # Oyun türlerini ayır ve tekrar eden türleri temizle
    genre_lists = []

    for g_str in df["genres"].values:
        temiz = clean_text(g_str)
        liste = []

        for g in temiz.split(";"):
            g = g.strip()

            if g and g not in liste:
                liste.append(g)

        genre_lists.append(liste)

    # 1. Oyun türlerinin görülme sayılarını hesapla
    genre_counts = {}

    for tags in genre_lists:
        for tag in tags:
            if tag in genre_counts:
                genre_counts[tag] += 1
            else:
                genre_counts[tag] = 1

    summary_df = pd.DataFrame(
        list(genre_counts.items()),
        columns=["Game_Type", "Count"]
    ).sort_values(by="Count", ascending=False)

    summary_df.to_csv("steam_game_genre_summary.csv", index=False)

    print("\n[+] Top 10 Game Types:")
    print(summary_df.head(10).to_string(index=False))

    # 2. Her oyun türü için bir indeks oluştur
    genre2idx = {}
    sayac = 0

    for tags in genre_lists:
        for genre in tags:
            if genre not in genre2idx:
                genre2idx[genre] = sayac
                sayac += 1

    # 3. TF matrisini oluştur ve normalize et
    game_count = len(genre_lists)
    vocab_size = len(genre2idx)
    tf = np.zeros((game_count, vocab_size))

    for i, tags in enumerate(genre_lists):
        for genre in tags:
            tf[i, genre2idx[genre]] += 1

        # Her oyunun tür sayısı farklı olduğu için TF değerlerini normalize et
        if len(tags) > 0:
            tf[i] = tf[i] / len(tags)

    # 4. Her türün bulunduğu oyun sayısını hesapla ve IDF değerlerini bul
    doc_freq = np.sum(tf > 0, axis=0)
    idf = np.log(game_count / doc_freq)

    # 5. TF ve IDF değerlerini çarparak TF-IDF matrisini oluştur
    tf_idf = tf * idf

    # Oyun türlerinin ortalama TF-IDF değerlerini hesapla
    tfidf_df = pd.DataFrame({
        "Game_Type": list(genre2idx.keys()),
        "Average_TF_IDF": tf_idf.mean(axis=0)
    }).sort_values(by="Average_TF_IDF", ascending=False)

    tfidf_df.to_csv("steam_game_tfidf_summary.csv", index=False)

    print("\n[+] Top 10 TF-IDF Game Types:")
    print(tfidf_df.head(10).to_string(index=False))
    print("\n[+] All operations completed!")


if __name__ == "__main__":
    main()
