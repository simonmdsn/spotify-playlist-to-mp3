import youtube_dl
import sys
import json
from pathlib import Path
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
import requests

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

passed = []


# list of urls
def youtube_to_mp3(urls):
    yt = youtube_dl.YoutubeDL(ydl_opts)
    yt.download(urls)


# name of youtube video
# returns youtube video id
# video id is the id after '?v='
# Eg. https://www.youtube.com/watch?v=K7-LndzNECs is K7-LndzNECs
def youtube_search(name):
    base = "https://www.youtube.com/results?search_query="
    qstring = quote(name)
    print("Searcing for", qstring)
    response = requests.get(base+qstring)
    soup = bs(response.text,'html.parser')
    vid = soup.find('a',attrs={'class':'yt-uix-tile-link'})
    if vid is None:
        passed.append(qstring)
    else:
        return vid['href'][9:]
