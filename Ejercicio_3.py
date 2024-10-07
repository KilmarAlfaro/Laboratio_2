import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("covid19.csv")
paises = df.groupby("Country/Region")["Confirmed"].sum()

top10_paises = paises.sort_values(ascending=False).head(10)

plt.pie(top10_paises, labels=top10_paises.index, autopct="%1.1f%%", startangle=90)
plt.title("Top 10 países con más casos de covid 19 confirmados")
plt.show()