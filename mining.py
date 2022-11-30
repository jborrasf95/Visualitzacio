import pandas as pd
import plotly.express as px

df = pd.read_csv("mtr.csv", sep=";")
print(df.columns)

fig = px.bar_polar(df, r="Average Tax Revenue", theta="Drug",
                    template="plotly_dark", color="Average Tax Revenue",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()