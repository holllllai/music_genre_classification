from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd

client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

genres = 'blues classical country disco hiphop jazz metal pop reggae rock electronic'.split()

playlists = '''5TkTomPbQuSNDxdlWg2fCx 37i9dQZF1DWWEJlAGA9gs0
            37i9dQZF1DXdfhOsjRMISB 3GqU5Q6CPUM7hM9ejxJC3z 33I6RpefRQcRh69xEczaKT 
            37i9dQZF1DX0SM0LYsmbMT 37i9dQZF1DXbl9rMxGEmRC 37i9dQZF1DWXti3N4Wp5xy
            37i9dQZF1DX8SfyqmSFDwe 37i9dQZF1DWXRqgorJj26U 15rhpIGkiReFt60lrCdzGI'''.split()

users = ['Filtr Legacy Sweden', 'Spotify', 'Spotify', 'Maarten de Lange', 'Leon Bouw', 'Spotify', 'Spotify', 'Spotify', 'Spotify', 
		'Spotify', 'kernkraftrecords']

columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 
           'acousticness', 'instrumentalness','liveness', 'valence', 'tempo', 'genre']

to_append = []
ids_lst = []
tracks_preview_lst = []
for g in zip(genres, users, playlists):
    
    # get playlist for given genre (default limit is 100)
    print('now the genre is ', g[0])
    track_ids = sp.user_playlist_tracks(g[1], playlist_id=g[2])
    # some lists for gathering data 
    tracks_id_lst = []
    for track in track_ids['items']:
        tracks_id_lst.append(track['track']['id'])
        ids_lst.append(track['track']['id'])
        tracks_preview_lst.append(track['track']['preview_url'])
    
    # get audio features for 50 tracks at a time (spotipy only allows 50 at once)
    # loop so all 100 tracks is included in the data
    for i in range(0,100, 50):
	    tracks_af = sp.audio_features(tracks_id_lst[i:i+50])
	    # print(len(tracks_af))
	    for track_num in range(0, 50):
	        track_data = []
	        print(track_num)
	        if tracks_af[track_num] == None:
	        	continue 
	        track_data.append(tracks_af[track_num]['danceability'])
	        track_data.append(tracks_af[track_num]['energy'])
	        track_data.append(tracks_af[track_num]['key'])
	        track_data.append(tracks_af[track_num]['loudness'])
	        track_data.append(tracks_af[track_num]['mode'])
	        track_data.append(tracks_af[track_num]['speechiness'])
	        track_data.append(tracks_af[track_num]['acousticness'])
	        track_data.append(tracks_af[track_num]['instrumentalness'])
	        track_data.append(tracks_af[track_num]['liveness'])
	        track_data.append(tracks_af[track_num]['valence'])
	        track_data.append(tracks_af[track_num]['tempo'])
	        track_data.append(g[0])
	        to_append.append(track_data)
audio_data = pd.DataFrame(to_append, columns=columns)
info = pd.DataFrame({'id':ids_lst, 'preview_url': tracks_preview_lst})
#concat id, preview_url information for each track
audio_data = pd.concat([info, audio_data], axis=1)
audio_data.to_csv('audio_data_new.csv')

