import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("covid19.csv")
paises = df.groupby("Country/Region")["Confirmed"].sum()

top10_paises = paises.sort_values(ascending=False).head(10)

plt.pie(top10_paises, labels=top10_paises.index, autopct="%1.1f%%", startangle=90)
plt.title("Top 10 países con más casos de covid 19 confirmados")
plt.show()

"""
Hola lic, para que esto le funcione debe descargar este archivo cvs de kaggles.com este es el enlace
https://www.kaggle.com/datasets/imdevskp/corona-virus-report
debe nombrarlo como "covid19.csv"

EN ESTE GRAFICO DE PASTEL LO QUE SE BUSCA ES SABER CUALES SON LOS 10 PAISES QUE HAN TENIDO MAS CASOS DE COVID 19 A LO LARGO DE LA PANDEMIA SIENDO 
US (estados unidos) el mayor con un % de 41.3
"""