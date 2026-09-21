import pandas as pd
from collections import Counter

def get_data():
    try:
        data = pd.read_csv("qa 2.csv")

        df_filtered = data.drop(columns=["id", "title", "bot_response", "user_question"])

        df_filtered.to_csv("filtered_data.csv")

    except FileExistsError as e:
        print("Can`t find file!", e)




get_data()
print("Data filtered successfully!")


def fetchActivityByDateAndTime():
    try:
        filedered_data = pd.read_csv("filtered_data.csv")

        filedered_data["datetime"] = pd.to_datetime(filedered_data["datetime"])

        target_month = "2026-04"

        date_filtered = filedered_data[filedered_data["datetime"].dt.strftime("%Y-%m") == target_month]

        date_filtered.to_csv("date_filtered.csv")

    except FileExistsError as e:
        print("Can`t find file!", e)



fetchActivityByDateAndTime()
print("Data filtered by date and time successfully!")