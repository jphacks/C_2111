import sys 
sys.path.append("./")
from goo_lab.goo_apis import Goo
import pandas as pd
from collections import Counter, defaultdict
from wordcloud import WordCloud

def create_wordcloud(csv_path:str="./user_data/user_data_sampled.csv", text_column_name:str = "tweet"):
    df = pd.read_csv(csv_path).sample(50).reindex()
    words_count = defaultdict(int)
    words = []
    app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
    g = Goo(app_id=app_id, request_id="record001")
    for text in df[text_column_name]:
        result = g.keyword(title="title", body = text).json()
        for i in result["keywords"]:
            words_count[list(i.keys())[0]]+=1
            words.append(list(i.keys())[0])
    text = ' '.join(words)
    fpath = "/usr/share/fonts/truetype/mplus/mplus-2c-bold.ttf"
    wordcloud = WordCloud(background_color="white",font_path=fpath,width=900, height=500).generate(text)
    wordcloud.to_file("./images/wordcloud.png")
