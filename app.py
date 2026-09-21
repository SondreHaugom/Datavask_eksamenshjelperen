import pandas as pd
from collections import Counter

def get_data():
    try:
        data = pd.read_csv("qa 2.csv")

        df_filtered = data.drop(columns=["id", "title", "bot_response", "user_question"])

        df_filtered.to_csv("filtered_data.csv",  index=False)

    except FileExistsError as e:
        print("Can`t find file!", e)






get_data()
print("Data filtered successfully!")


def fetchActivityByDateAndTime():
    try:
        filedered_data = pd.read_csv("filtered_data.csv")

        date_filtered = filedered_data.loc["2025-10-21" :  "2026-08-20"]

        date_filtered.to_csv("date_filtered.csv", index=False)

    except FileExistsError as e:
        print("Can`t find file!", e)



fetchActivityByDateAndTime()
print("Data filtered by date and time successfully!")