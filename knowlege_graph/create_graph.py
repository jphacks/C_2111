import sys 
sys.path.append("./")
from goo_lab.goo_apis import Goo
import pandas as pd
from collections import Counter, defaultdict
from wordcloud import WordCloud

df = pd.read_csv("./user_data/user_data_sampled.csv").sample(50).reindex()

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
print("固有表現抽出")
g = Goo(app_id=app_id, request_id="record001")


# for text in df["tweet"]:
#     result = g.entity(sentence=text, class_filter="PSN|ORG").json()
#     print(result["ne_list"])

print("キーワード")
for title, text in zip(df["username"],df["tweet"]):
    result = g.keyword(title=title, 
    body = text).json()
    print(result)
    print(result["keywords"])

def counter(texts_list: list):
    words_count = defaultdict(int)
    words = []
    for text in texts_list:
        result = g.keyword(title=title, 
        body = text).json()
        words_count
