import plotly.graph_objects as go
from collections import Counter, defaultdict
import pandas as pd
from goo_lab.goo_apis import Goo
from itertools import count
from PIL import Image
import io
import base64
import sys
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
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=list(count_result.keys()), y=list(count_result.values()))
    )
    fig.update_layout(title="特定名詞の出現回数。", xaxis={
                      'categoryorder': 'total descending'})
    return fig.to_html(full_html=False, include_plotlyjs=False)
