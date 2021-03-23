import plotly.figure_factory as pf
import pandas as pd
import csv

data = pd.read_csv('data.csv')

fig = pf.create_distplot([data['Avg Rating'].tolist()],['Ratings'])
fig.show()