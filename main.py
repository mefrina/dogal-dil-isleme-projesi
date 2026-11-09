import re
import pandas as pd
import numpy as np

def clean_text(text):
    if pd.isna(text):
        return ""

    text = str(text)
    text = text.replace("Â", "a").replace("â", "a")
    text = text.replace("î", "i").replace("Î", "i")
    text = text.replace("İ", "i")

    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)

    # Noktalı virgülü türleri ayırmak için koru
    text = re.sub(r"[^A-Za-z0-9;âîığüşöçİĞÜŞÖÇ]+", " ", text)

    return " ".join(text.lower().strip().split())


def main():
    print("[+] Loading dataset...")
    df = pd.read_csv("data_set")
    print(f"[+] Total games: {len(df)}")

    if "genres" not in df.columns:
        print("[-] genres column not found!")
        return

    # Oyun türlerini temizle ve ayır
    genre_lists = df["genres"].apply(
        lambda x: list(dict.fromkeys(
            g.strip() for g in clean_text(x).split(";") if g.strip()
        ))
    )

    # 1. Oyun türlerinin sayımı
    genre_counts = {}
    for tags in genre_lists:
        for tag in tags:
            genre_counts[tag] = genre_counts.get(tag, 0) + 1

    summary_df = pd.DataFrame(
        list(genre_counts.items()),
        columns=["Game_Type", "Count"]
    ).sort_values(by="Count", ascending=False)

    summary_df.to_csv(
        "steam_game_genre_summary.csv", index=False, encoding="utf-8-sig"
    )

    print("\n[+] Top 10 Game Types:")
    print(summary_df.head(10).to_string(index=False))

    # 2. Oyun türleri için indeks sözlüğü oluştur
    genre2idx = {}
    for tags in genre_lists:
        for genre in tags:
            if genre not in genre2idx:
                genre2idx[genre] = len(genre2idx)

    # 3. TF matrisi
    game_count = len(genre_lists)
    vocab_size = len(genre2idx)
    tf = np.zeros((game_count, vocab_size))

    for i, tags in enumerate(genre_lists):
        for genre in tags:
            tf[i, genre2idx[genre]] += 1

        # Her oyunun tür sayısı farklı olabileceği için TF değerlerini toplam tür sayısına böldüm.
        if tags:
            tf[i] /= len(tags)

    # 4. IDF vektörü
    doc_freq = np.sum(tf > 0, axis=0)
    idf = np.zeros(vocab_size)
    valid = doc_freq > 0
    idf[valid] = np.log(game_count / doc_freq[valid])

    # 5. TF-IDF matrisi
    tf_idf = tf * idf

    # Türlerin ortalama TF-IDF değerlerini hesapla
    tfidf_df = pd.DataFrame({
        "Game_Type": list(genre2idx.keys()),
        "Average_TF_IDF": tf_idf.mean(axis=0)
    }).sort_values(by="Average_TF_IDF", ascending=False)

    tfidf_df.to_csv(
        "steam_game_tfidf_summary.csv", index=False, encoding="utf-8-sig"
    )

    print("\n[+] Top 10 TF-IDF Game Types:")
    print(tfidf_df.head(10).to_string(index=False))
    print("\n[+] All operations completed!")
    

if __name__ == "__main__":
    main()
