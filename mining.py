import pandas as pd
import plotly.express as px

df = pd.read_csv("Registre_de_casos_de_COVID-19_a_Catalunya_per_municipi_i_sexe.csv", sep=",")


df[["dia","mes", "any"]] =  df["TipusCasData"].str.split("/", 2, expand=True)

print(df.columns)
df_sabadell = df[df["MunicipiDescripcio"] == "SABADELL"]

df_clean = df_sabadell[["mes", "SexeDescripcio", "NumCasos"]]

df_mensual = df_clean.groupby(["mes", "SexeDescripcio"]).mean().reset_index()


fig = px.bar_polar(df_mensual, r="NumCasos", theta="mes",
                    template="plotly_dark", color="SexeDescripcio",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()


