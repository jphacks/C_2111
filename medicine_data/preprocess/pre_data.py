import pandas as pd
import numpy as np
import os
import glob

files = glob.glob("*.csv")
df = pd.DataFrame()
for i in files:
    tmp_df = pd.read_csv(i)
    df = pd.concat([df, tmp_df], axis = 0)

df = df.query("target == 1")[["username", "tweet"]]

print(df.shape)

df.to_csv("../user_data.csv", index = False)