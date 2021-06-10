import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("csv.csv")
fig=ff.create_distplot([df["Brand"].tolist()],["Brand"],show_hist=False)
fig.show()