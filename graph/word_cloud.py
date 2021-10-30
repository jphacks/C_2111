from wordcloud import WordCloud
from collections import Counter, defaultdict
import pandas as pd
from goo_lab.goo_apis import Goo
import sys
import io
import base64
from PIL import Image
sys.path.append("./")


def create_wordcloud(texts):
    words_count = defaultdict(int)
    words = []
    app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
    g = Goo(app_id=app_id, request_id="record001")
    for text in texts:
        result = g.keyword(title="title", body=text).json()
        for i in result["keywords"]:
            words_count[list(i.keys())[0]] += 1
            words.append(list(i.keys())[0])
    text = ' '.join(words)
    fpath = "/usr/share/fonts/truetype/mplus/mplus-2c-bold.ttf"
    wordcloud = WordCloud(background_color="white",
                          font_path=fpath, width=900, height=500).generate(text)
    wordcloud.to_file("./images/wordcloud.png")


def create_wordcloud_base64(texts):
    words_count = defaultdict(int)
    words = []
    app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
    g = Goo(app_id=app_id, request_id="record001")
    for text in texts:
        result = g.keyword(title="タイトル", body=text).json()
        for i in result["keywords"]:
            words_count[list(i.keys())[0]] += 1
            words.append(list(i.keys())[0])
    if len(words) == 0:
        return None
    text = ' '.join(words)
    fpath = "/usr/share/fonts/truetype/mplus/mplus-2c-bold.ttf"
    wordcloud = WordCloud(background_color="white",
                          font_path=fpath, width=900, height=500).generate(text)
    image_array = wordcloud.to_array()
    img = Image.fromarray(image_array)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    base64Img = base64.b64encode(buf.getvalue()).decode().replace("'", "")
    return base64Img
