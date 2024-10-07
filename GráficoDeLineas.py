import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('GIStats.csv')

top_characters = data.nlargest(10, 'Base ATK')


plt.figure(figsize=(10, 6))

plt.plot(top_characters['Character'], top_characters['Base ATK'], marker='o')


plt.title('10 personajes de Genshin Impact con su respectivo Ataque Base', fontsize=16)

plt.xlabel('Nombre del Personaje', fontsize=12)

plt.ylabel('Ataque Base', fontsize=12)

plt.xticks(rotation=45) 

plt.grid()


plt.tight_layout()
plt.show()


""" El dataset de este abajo:
https://www.kaggle.com/datasets/genshinplayer/genshin-impact-characters-stats
Cuando lo descargue le cambia el nombre a GIStats.csv

Este gráfico muestra la estadística de ataque base de 10 personajes del juego que se llama Genshin Impact

y a diferencia del ejercicio de spotify este si me permitio utilizar el metodo convencional """