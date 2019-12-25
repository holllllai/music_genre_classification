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
info = sp.user('Spotify')
print(info)

{'added_at': '2018-10-19T14:32:27Z', 
'added_by': {'external_urls': 
							{'spotify': 'https://open.spotify.com/user/thesoundsofspotify'}, 
			'href': 'https://api.spotify.com/v1/users/thesoundsofspotify', 
			'id': 'thesoundsofspotify', 
			'type': 'user', 
			'uri': 'spotify:user:thesoundsofspotify'}, 
'is_local': False, 
'primary_color': None, 
'track': {'album': 
					{'album_type': 'album', 
					'artists': 
								[{'external_urls': 
													{'spotify': 'https://open.spotify.com/artist/52GxmJdAcByy1ZyPivpUns'}, 
								'href': 'https://api.spotify.com/v1/artists/52GxmJdAcByy1ZyPivpUns', 
								'id': '52GxmJdAcByy1ZyPivpUns', 
								'name': 'Lonnie Mack', 
								'type': 'artist', 
								'uri': 'spotify:artist:52GxmJdAcByy1ZyPivpUns'}],
								'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 
														'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE',
													 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 
													 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 
													 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 
													 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 
													 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 
													 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'],
					 'external_urls': {'spotify': 'https://open.spotify.com/album/0HqOAmtjJT9BlHCmnH0ILa'}, 
					 'href': 'https://api.spotify.com/v1/albums/0HqOAmtjJT9BlHCmnH0ILa', 
					 'id': '0HqOAmtjJT9BlHCmnH0ILa', 
					 'images': 
					 			[{'height': 640, 
					 			'url': 'https://i.scdn.co/image/ab67616d0000b273f4d9d72f2f1f59212b2ca1a2', 
					 			'width': 640}, 
					 			{'height': 300, 
					 			'url': 'https://i.scdn.co/image/ab67616d00001e02f4d9d72f2f1f59212b2ca1a2', 
					 			'width': 300}, 
					 			{'height': 64,
					 			 'url': 'https://i.scdn.co/image/ab67616d00004851f4d9d72f2f1f59212b2ca1a2', 
					 			 'width': 64}],
					  'name': 'The Hills Of Indiana',
					  'release_date': '2006-08-22', 
					  'release_date_precision': 'day',
					  'total_tracks': 12,
					  'type': 'album',
					  'uri': 'spotify:album:0HqOAmtjJT9BlHCmnH0ILa'}, 
					  'artists': [{'external_urls':
					  			 {'spotify': 'https://open.spotify.com/artist/52GxmJdAcByy1ZyPivpUns'}, 
					  			 'href': 'https://api.spotify.com/v1/artists/52GxmJdAcByy1ZyPivpUns',
					  			  'id': '52GxmJdAcByy1ZyPivpUns', 
					  			  'name': 'Lonnie Mack',
					  			  'type': 'artist', 
					  			  'uri': 'spotify:artist:52GxmJdAcByy1ZyPivpUns'}],
					  			  'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 
					  			  'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY'
					  			  , 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 
					  			  'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 
					  			  'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 
					  			  'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 
					  			  'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 
					  			  'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY',
					  			   'VN', 'ZA'],
		'disc_number': 1, 
		'duration_ms': 192746, 
		'episode': False,
		 'explicit': False, 
		 'external_ids': 
		 				{'isrc': 'USEE10251287'}, 
		 'external_urls': {'spotify': 'https://open.spotify.com/track/3lzYygPp67p7T9QDdrLja5'}, 
		 'href': 'https://api.spotify.com/v1/tracks/3lzYygPp67p7T9QDdrLja5',
		  'id': '3lzYygPp67p7T9QDdrLja5',
		   'is_local': False,
		    'name': 'Rings', 
		    'popularity': 45, 
		    'preview_url': 'https://p.scdn.co/mp3-preview/6734fad25d9e3e0529750386808c340e10623341?cid=5753b92e6a084808bea42ea533c53400', 
		    'track': True, 
		    'track_number': 8, 
		    'type': 'track', 
		    'uri': 'spotify:track:3lzYygPp67p7T9QDdrLja5'}, 
		    'video_thumbnail': {'url': None}}