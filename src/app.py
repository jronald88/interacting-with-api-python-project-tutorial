#!pip install spotipy
#!pip install python-dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import matplotlib.pyplot as plt
import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
client_credentials_manager=SpotifyClientCredentials(client_id, client_secret)
connection = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print(connection)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
result = sp.artist_top_tracks("0WwSkZ7LtFUFjGjMZBMt6T")
print(result.keys())
print(type(result["tracks"]))
tracks = result["tracks"][0:10]
#print(tracks)
sub_tracks = [(d["name"],d["popularity"],d["duration_ms"]) for d in tracks]
print(sub_tracks)
columns = ["Track", "Popularity", "Duration"]

df = pd.DataFrame(sub_tracks,columns=columns)

print(df.head(3))

x_vals = df.Popularity
y_vals = df.Duration

plt.scatter(x_vals,y_vals)
plt.show()
plt.savefig("Scatter.jpg",dpi = 300)
corr = df.corr()
print(corr)