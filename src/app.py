import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

print(client_id, client_secret)

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

artist_id = "3Nrfpe0tUJi4K4DXYWgMUX"

# Función para obtener el top 10 de canciones del artista
def get_top_tracks(artist_id):
    results = spotify.artist_top_tracks(artist_id)
    tracks = results["tracks"][:10]  # Top 10 canciones
    return [
        {
            "nombre": track["name"],
            "popularidad": track["popularity"],
            "duracion_minutos": round(track["duration_ms"] / 60000, 2)
        }
        for track in tracks
    ]
top_tracks = get_top_tracks(artist_id)
top_tracks

df = pd.DataFrame(top_tracks)

# Ordenar por popularidad creciente
df_sorted = df.sort_values(by="popularidad", ascending=True)

# Mostrar el top 3 más popular
top_3 = df_sorted.head(3)
top_3

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="duracion_minutos", y="popularidad", marker='o', color='b')

# Título y etiquetas
plt.title('Relación entre la duración y la popularidad de las canciones de BTS')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')

# Mostrar el gráfico
plt.show()

# Conclusión: No hay una relación clara entre la duración de las canciones y su popularidad en BTS.
# El gráfico muestra una dispersión de puntos, lo que sugiere que otros factores, como la calidad de la producción y 
# la conexión con los fanáticos, juegan un papel más importante que la duración en el éxito de las canciones.