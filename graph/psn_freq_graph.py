from itertools import count
import sys
sys.path.append("./")
from goo_lab.goo_apis import Goo
import pandas as pd
from collections import Counter, defaultdict
import plotly.graph_objects as go

app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
g = Goo(app_id=app_id, request_id="record001")#.entity(sentence=sentence, class_filter="PSN")

def create_psn_freq_graph(csv_path:str="./user_data/user_data_sampled.csv", text_column_name:str = "tweet"):
    df = pd.read_csv(csv_path).sample(1000).reindex()
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
fig.show()