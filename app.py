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
            (filedered_data["datetime"].dt.strftime("%H:%M") >= "15:00")
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

    # Tell antall spørringer per time (dato + klokkeslett), sortert i tid
    diagram_data["dato_time"] = diagram_data["datetime"].dt.floor("h")
    query_count = diagram_data.groupby("dato_time").size().sort_index()

    plt.figure(figsize=(10, 6))
    plt.bar(query_count.index.strftime("%d.%m %H:%M"), query_count.values)

    plt.title("Antall spørringer over tid")
    plt.xlabel("Dato og klokkeslett")
    plt.ylabel("Antall spørringer")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


diagram()