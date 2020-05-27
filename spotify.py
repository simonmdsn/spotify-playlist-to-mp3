import requests
import json
import secrets

def get_all_tracks_in_playlist(playlist_id):
    token = secrets.get_spotify_token()
    url = 'https://api.spotify.com/v1/playlists/' + str(playlist_id).split(':')[2] + '/tracks'
    headers = {'Authorization': 'Bearer ' + token, 'content-type':'application/json'}
    response = requests.get(url=url,headers=headers)
    return [item['track']['name'] + " " + item['track']['artists'][0]['name'] for item in response.json()['items']]