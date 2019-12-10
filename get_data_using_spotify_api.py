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

playlists = '''7qACZGMjyo64TdUdKAegjp 3HYK6ri0GkvRcM6GkKh0hJ 
            4mijVkpSXJziPiOrK7YX4M 0ZVSWcJIf7cvycEn9HUvps 6MXkE0uYF4XwU4VTtyrpfP 
            5EyFMotmvSfDAZ4hSdKrbx 3pBfUFu8MkyiCYyZe849Ks 6gS3HhOiI17QNojjPuPzqc 
            0TcXdt4sbITbwCwwFbKYyd 7dowgSWOmvdpwNkGFMUs6e 6I0NsYzfoj7yHXyvkZYoRx'''.split()

columns = ['id','danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 
           'acousticness', 'instrumentalness','liveness', 'valence', 'tempo', 'genre']

to_append = []

for g in zip(genres, playlists):
    
    # get playlist for given genre (default limit is 100)
    track_ids = sp.user_playlist_tracks('thesoundsofspotify', playlist_id=g[1], 
                                        fields='items(track(id))')
    # some lists for gathering data 
    tracks_list = []
    
    for track in track_ids['items']:
        tracks_list.append(track['track']['id'])
    
    # get audio features for 50 tracks at a time (spotipy only allows 50 at once)
    # code below can be looped if more tracks need to be analyzed
    tracks_af = sp.audio_features(tracks_list[:50])
    for track_num in range(0, 50):
        track_data = []
        track_data.append(tracks_af[track_num]['id'])
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
print(tracks_af[0])
# print(len(tracks_list))
