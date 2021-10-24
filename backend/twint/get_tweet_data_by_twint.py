import os
import re

# from wtfml.auth.twitter_api import get_twiiter_api
import time
from datetime import datetime
from re import T

import neologdn
import nest_asyncio
import pandas as pd
import requests
import twint
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
from tqdm import tqdm

nest_asyncio.apply()
since = None
until = None
month_delta = 1
q = "死にたい"
save_folder = "../data"
save_path = os.path.join(save_folder, f"{q}.csv")

since = since or datetime.strftime(
    datetime.today() - relativedelta(months=month_delta), "%Y-%m-%d"
    )
print(since)
until = until or datetime.strftime(datetime.today(), "%Y-%m-%d")
print(until)
limit = 500
# Configure
c = twint.Config()
c.Search = q
c.Limit = limit
c.Store_object = True
c.Pandas = True
c.User_full = True
c.Since = since
c.Until = until

# Run
print("start run")
twint.run.Search(c)
print("end run")


search_result_df = twint.storage.panda.Tweets_df
search_result_df = search_result_df.drop_duplicates(subset="username").reset_index()
print("検索終わり")

"""
以下特定の条件を消したいとき利用
"""
# regex_list = [r"[0-9][0-9]", r"[0-9]X", r"[0-9]x"]
# regex_compilers = [re.compile(regex) for regex in regex_list]
# url_patterns = re.compile(r"http\S+")
# anti_regex_list = [
#     # r"[0-9][0-9][0-9]",
#     # r":[0-9][0-9]",
#     # r"[0-9][0-9]月",
#     # r"[0-9][0-9]日",
#     # r"[0-9]年",
#     # r"[0-9]時間",
#     # r"[0-9]時",
#     # r"[0-9]分",
#     r"[0-9]秒",
# ]
# anti_regex_compilers = [re.compile(regex) for regex in anti_regex_list]


# final_result = []
# for i, search_result in search_result_df.iterrows():

#     tweet_text = neologdn.normalize(search_result["tweet"])
#     tweet_text = re.sub(url_patterns, "", tweet_text)
#     # if "歳になりました" not in tweet_text or tweet_text[0] == "@":
#         # continue
#     anti_sig = False
#     for anti_regex_compiler in anti_regex_compilers:
#         if anti_regex_compiler.search(tweet_text):
#             anti_sig = True
#             break
#     if anti_sig:
#         continue

#     for regex_compiler in regex_compilers:
#         regex_search_result = regex_compiler.findall(tweet_text)
#         if regex_search_result:
#             search_result_dict = search_result.to_dict()
#             search_result_dict["age"] = regex_search_result[-1]
#             if f"{regex_search_result[-1]}代" in tweet_text:
#                 search_result_dict["age"] = f"{regex_search_result[-1]}代"
#             search_result_dict["is_last"] = True if "最後" in tweet_text else False

#             final_result.append(search_result_dict)
#             break
# search_result_df = pd.DataFrame(final_result)



# anti_list = [
# ]

# for i, search_result in search_result_df.iterrows():
#     for anti in anti_list:
#         if anti in search_result["tweet"]:
#             search_result_df.drop(index = i, inplace = True)
#             break


print(len(search_result_df))
search_result_df.to_csv(save_path, encoding = "utf-8")
