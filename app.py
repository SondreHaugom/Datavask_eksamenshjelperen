import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    try:
        data = pd.read_csv("qa 2.csv")

        df_filtered = data.drop(columns=["id", "title", "bot_response", "user_question"])

        df_filtered.to_csv("filtered_data.csv", index=False)

    except FileNotFoundError as e:
        print("Can`t find file!", e)


get_data()
print("Data filtered successfully!")


def fetchActivityByDateAndTime():
    try:
        filedered_data = pd.read_csv("filtered_data.csv")

        filedered_data["datetime"] = pd.to_datetime(filedered_data["datetime"])

        target_month = "2026-05" 

        date_filtered = filedered_data[
            (filedered_data["datetime"].dt.strftime("%Y-%m") >= target_month) &
            (
                (filedered_data["datetime"].dt.strftime("%H:%M") >= "15:00") |
                (filedered_data["datetime"].dt.dayofweek >= 5)
            )
        ]


        date_filtered.to_csv("date_filtered.csv", index=False)

    except FileNotFoundError as e:
        print("Can`t find file!", e)


fetchActivityByDateAndTime()
print("Data filtered by date and time successfully!")







def diagram():
    diagram_data = pd.read_csv("date_filtered.csv")

    diagram_data["datetime"] = pd.to_datetime(
        diagram_data["datetime"],
        errors="coerce"
    )

    # Fjern rader uten gyldig tidspunkt
    diagram_data = diagram_data.dropna(subset=["datetime"])

    # Kategoriser hver spørring som helg eller kveldstid (hverdag)
    is_weekend = diagram_data["datetime"].dt.dayofweek >= 5
    diagram_data["kategori"] = is_weekend.map({True: "Helg", False: "Kveldstid (hverdag)"})

    query_count = diagram_data["kategori"].value_counts()

    plt.figure(figsize=(8, 6))
    plt.bar(query_count.index, query_count.values, color=["#4C72B0", "#DD8452"])

    plt.title("Spørringer utenfor arbeidstid: helg vs. kveldstid")
    plt.xlabel("Kategori")
    plt.ylabel("Antall spørringer")

    plt.tight_layout()
    plt.show()


diagram()