import plotly.graph_objects as go
from collections import Counter, defaultdict
import pandas as pd
import numpy as np
from goo_lab.goo_apis import Goo
from itertools import count
from PIL import Image
import io
import base64
import sys
import matplotlib.pyplot as plt
import japanize_matplotlib
sys.path.append("./")

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
# .entity(sentence=sentence, class_filter="PSN")
g = Goo(app_id=app_id, request_id="record001")


def create_psn_freq_graph_base64(texts):
    l = []
    for text in texts:
        result = g.entity(sentence=text, class_filter="PSN").json()
        for i in result["ne_list"]:
            l.append(i[0])

    count_result = Counter(l)

    fig, ax = plt.subplots()
    plt.bar(list(count_result.keys()), sorted(list(count_result.values())))
    plt.xticks(rotation=90)
    plt.xlabel("固有名詞")
    plt.ylabel("出現回数")
    plt.show()

    fig.canvas.draw()
    im = np.array(fig.canvas.renderer.buffer_rgba())

    img = Image.fromarray(im)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    base64Img = base64.b64encode(buf.getvalue()).decode().replace("'", "")
    return base64Img
