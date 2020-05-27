import json
import base64
import requests

secrets_json = json.load(open('secrets.json'))
spotify_id = secrets_json['spotify_id']
spotify_secret = secrets_json['spotify_secret']
spotify_base64 = base64.b64encode(bytes(
    secrets_json['spotify_id'] + ":" + secrets_json['spotify_secret'], 'utf-8')).decode()


def get_spotify_token():
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url='https://accounts.spotify.com/api/token', data=data, auth=(
        spotify_id, spotify_secret), headers={'content-type': 'application/x-www-form-urlencoded'})
    spotify_token = str(response.json()['access_token'])
    return response.json()['access_token']
