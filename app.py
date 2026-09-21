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
