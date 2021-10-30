import nlplot 
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv('../user_data/user_data.csv')
npt = nlplot.NLPlot(df, target_col='tweet')
stopwords = npt.get_stopword(top_n=10, min_freq=0)
npt.build_graph(stopwords=stopwords, min_edge_frequency=25)
# 全データ・#データサイエンティスト・#kaggleをそれぞれインスタンス化

npt.build_graph(stopwords=stopwords, min_edge_frequency=25)
npt.co_network(
    title='Co-occurrence network', save = True
)
