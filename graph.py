import pandas as pd
import plotly.express as px

df = pd.read_csv("F:\Saanvi\Python\class projects\c 103\Copy+of+data+-+data.csv")
fig = px.scatter(df, x="date", y="cases",color="country",title='Corona Cases')
fig.show()
#made by saanvi