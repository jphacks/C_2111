# 鬱の薬を使っている人からのスクレイピング
import twint
import os
import pandas as pd

df = pd.read_csv("../medicine_data/user_data.csv").query(
    "username != 'science_Lv14'"
)
user_name_list = df["username"]

save_folder = "../user_data"
os.makedirs(save_folder, exist_ok=True)
save_path = os.path.join(save_folder, "user_data.csv")
df = pd.DataFrame()
for user_name in user_name_list:
    # Configure
    c = twint.Config()
    c.Username = user_name
    c.Store_object = True
    c.Pandas = True
    c.User_full = True

    # Run
    twint.run.Search(c)
    try:
        search_result_df = twint.storage.panda.Tweets_df
        search_result_df = search_result_df.reset_index()
        print(search_result_df.shape)
        df = pd.concat([df, search_result_df], axis = 0)
        df.to_csv(save_path, encoding = "utf-8")
    except ValueError as error:
        print(error)
        continue



print(save_path)
print("Done saving!")