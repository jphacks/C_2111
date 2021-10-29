# 学習用データを作成する

import pandas as pd

df = pd.read_csv("../user_data/user_data.csv").sample(30000).reindex()
df["target"] = 1
df_shinitai = pd.read_csv("../data/死にたい.csv").reindex()
df_fuan = pd.read_csv("../data/不安 学校.csv").reindex()
df_ikitaku = pd.read_csv("../data/学校 行きたくない.csv").reindex()
df = pd.concat([df , df_fuan, df_shinitai, df_ikitaku], axis = 0)
df = df[["username","tweet","target"]]

df_no_utsu = pd.read_csv("../user_data/no_utsu.csv").sample(5000).reindex()
df_fun = pd.read_csv("../data/楽しい.csv").sample(5000).reindex()
df_desu = pd.read_csv("../data/です.csv").sample(5000).reindex()
df_happy = pd.read_csv("../data/うれしい.csv").sample(5000).reindex()


df_no_utsu = pd.concat([df_no_utsu, df_fun, df_desu, df_happy], axis = 0)

df_no_utsu["target"] = 0
df_utsu = df_no_utsu[["username","tweet","target"]]

df = pd.concat([df, df_utsu], axis = 0)

print(df.head())
df.to_csv("../user_data/train_data_sampled.csv")
print(df.shape)