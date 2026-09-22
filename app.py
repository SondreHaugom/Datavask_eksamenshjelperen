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
    diagram_data["kategori"] = is_weekend.map({True: "Helg", False: "Kveldstid (hverdag, etter kl. 15)"})

    query_count = diagram_data["kategori"].value_counts()
    query_count = query_count.reindex(
        ["Kveldstid (hverdag, etter kl. 15)", "Helg"], fill_value=0
    )

    periode_start = diagram_data["datetime"].min().strftime("%d.%m.%Y")
    periode_slutt = diagram_data["datetime"].max().strftime("%d.%m.%Y")

    farger = ["#2a78d6", "#eb6834"]
    etiketter = ["Kveldstid\n(man–fre, etter kl. 15)", "Helg\n(lør–søn, hele døgnet)"]

    _, ax = plt.subplots(figsize=(8, 6))
    stolper = ax.bar(etiketter, query_count.values, color=farger)

    # Vis antall over hver stolpe
    ax.bar_label(stolper, padding=3, fontsize=11, fontweight="bold")

    ax.set_title("Spørringer utenfor arbeidstid: helg vs. kveldstid")
    ax.text(
        0.5, 1.02,
        f"Periode: {periode_start} – {periode_slutt}",
        transform=ax.transAxes, ha="center", fontsize=9, color="#52514e",
    )
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Antall spørringer")

    plt.tight_layout()
    plt.show()


diagram()