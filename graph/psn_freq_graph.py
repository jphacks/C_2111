<<<<<<< HEAD
from itertools import count
import sys
sys.path.append("./")
from goo_lab.goo_apis import Goo
import pandas as pd
from collections import Counter, defaultdict
import plotly.graph_objects as go

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
g = Goo(app_id=app_id, request_id="record001")

def create_psn_freq_graph(csv_path:str="./user_data/user_data_sampled.csv", text_column_name:str = "tweet"):
    df = pd.read_csv(csv_path).sample(100).reindex()
    l = []
    for text in df[text_column_name]:
        result = g.entity(sentence=text, class_filter="PSN").json()
        for i in result["ne_list"]:
            l.append(i[0])
    return Counter(l)

count_result  = create_psn_freq_graph()
fig = go.Figure()
fig.add_trace(
    go.Bar(x = list(count_result.keys()), y = list(count_result.values()))
)

fig.update_layout(title = "特定名詞の出現回数。", xaxis={'categoryorder':'total descending'})
print(fig.to_html(include_plotlyjs=False))
=======
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
>>>>>>> b7cd7e9d01843d2cef27f693058c3d70cd6257d8
