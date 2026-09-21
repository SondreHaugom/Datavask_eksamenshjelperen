import pandas as pd

def get_data():
    data = pd.read_csv("qa 2.csv")
    if data.empty:
        print("No data found.")
    else:
        return data


def get_question():
    filtered_colums = ["id", "title", "user_question", ]