import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("F:\Saanvi\Python\class projects\c 103\Copy+of+data+-+data.csv")
fig = px.bar(df, x='date', y='cases',color='country', title='Corona cases')
fig.show()
#made by saanvi