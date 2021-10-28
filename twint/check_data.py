import pandas as pd

df = pd.read_csv("../user_data/user_data.csv").sample(20000).reindex()
df["target"] = 1
df = df[["username","tweet","target"]]

df_utsu = pd.read_csv("../user_data/no_utsu.csv").sample(20000).reindex()
df_utsu["target"] = 0
df_utsu = df_utsu[["username","tweet","target"]]

df = pd.concat([df, df_utsu], axis = 0)

print(df.head())
df.to_csv("../user_data/train_data_sampled.csv")
print(df.shape)