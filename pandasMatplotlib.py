import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('spotify.csv', encoding='latin1')


df = df.dropna(subset=['track_name'])


top_songs = df.sort_values(by='streams', ascending=True).head(10)


plt.figure(figsize=(12, 6))  
plt.bar(top_songs['track_name'], top_songs['streams'], color='skyblue')
plt.xlabel('Canciones')
plt.ylabel('Reproducciones')
plt.title('Las 10 canciones con mas reproducciones de Spotify')


y_ticks = plt.yticks()[0]


filtered_ticks = [tick for tick in y_ticks if tick > min(y_ticks)]
plt.yticks(filtered_ticks)


plt.xticks(rotation=45, ha='right')


plt.subplots_adjust(bottom=0.25)

plt.tight_layout()  
plt.show()



""" Lic le dejo la dataset de este ejercicio 
https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download

cuando lo descargue le cambia el nombre a solamente spotify por que me resulto más fácil de ver

Este Gráfico es de barras y utiliza el dataset de las canciones como más reproducciones que hay en spotify
pero para propositos prácticos solo utilizamos las 10 canciones con más reproducciones que muestra el número
de reproducciones (streams) y el nombre de la canción solamente


PD: Tambien busque por que no podía utilizar bien esta dataset y encontré que hay algunas que no 
corren con el método normal y convencional que es el UTP-8 asi que decidí utiliar encoding='latin1'
aunque también pude haber utilizado ISO-8859-1
"""