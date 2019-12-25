12/09
creating a new repository for music genre classification project.
The first step is to gather data from spotify api - gather id, genre, audio feature, and 30 seconds audio samples.
Goal is to create a get_data_using_spotify_api.py 
in order to use the spotify web api, 'pip install spotipy' as a start 

need to know how to get music from each genre. Yash Duo's post uses different playlists.. how did he get the playlists ids? and how to readjust the limits? 

12/10
succesfully created dataset including audio analysis, id, and preview_url! woo-hoo! now need to check if there's any missing value, and check if each genre has 100 tracks.

there are 360 null values of preview urls.... need to recollect data


blues         140
classical     114
country       115
disco         114
electronic    173
hiphop         89
jazz          123
metal         176
pop           102
reggae        132
rock           85
dtype: int64

collected more data with preview urls... need to still collect more in the hiphop genre and the rock genre