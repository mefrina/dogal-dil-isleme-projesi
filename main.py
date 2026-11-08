import re
import pandas as pd


def clean_text(text):

    text = text.replace("Â", "a")
    text = text.replace("â", "a")
    text = text.replace("î", "i")
    text = text.replace("Î", "ı")
    text = text.replace("İ", "i")
    text = text.replace("I", "ı")

    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[^A-Za-z0-9âîığüşöçİĞÜŞÖÇ]+", " ", text)

    return " ".join(text.lower().strip().split())


def main():
    print("[+] starting script...")
    print("[+] loading the data_set")
    df = pd.read_csv("data_set") #reads the data set
    print(f"[+] Total rows loaded: {len(df)}")

    if "genres" in df.columns:
        df["clean_genres"] = df["genres"].apply(clean_text)
    else:
        print("[-] could not find genres in dataset!")
        exit()

    # 3. Do Stuff: Count frequencies of specific game genres/types
    genre_counts = {}
    for genre_entry in df["clean_genres"]:
        if ";" in genre_entry:
            tags = genre_entry.split(";")
        else:
            tags = genre_entry.split(" ")

        for tag in tags:
            tag = tag.strip()
            if tag not in genre_counts:
                genre_counts[tag] = 1
            else:
                genre_counts[tag] = genre_counts[tag] + 1


    game_types = []
    total_counts = []
    
    for key, val in genre_counts.items():
        game_types.append(key)
        total_counts.append(val)

    summary_df = pd.DataFrame()
    summary_df["Game_Type"] = game_types
    summary_df["Count"] = total_counts

        #sort by decending
    summary_df = summary_df.sort_values(by="Count", ascending=False)

    output_filename = "steam_genre_summary.csv"
    summary_df.to_csv(output_filename, index=False)

    print(f"\n[+] Successfully saved game type counts to '{output_filename}'!")
    
    # Print the top 10 rows one-by-one or using a simple head
    print("\n[+] Top 10 Game Types/Genres:")
    top_ten = summary_df.head(10)
    print(top_ten.to_string(index=False))


main() #run the script
