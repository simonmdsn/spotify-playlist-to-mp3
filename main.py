import youtube
import spotify
import sys
from pathlib import Path
import glob
import shutil
import os
import random
import string

playlist_id = sys.argv[1]


# move mp3s to music folder
def move_mp3_to_music():
    Path('music').mkdir(parents=True, exist_ok=True)
    files = glob.glob('*mp3')
    for mp3 in files:
        if not Path('music/' + mp3).is_file():
            shutil.move(mp3, 'music')
        else:
            new = mp3[:len(mp3)-4] + random_string() + ".mp3"
            os.rename(mp3, new)
            shutil.move(new, 'music')


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


tracks = spotify.get_all_tracks_in_playlist(playlist_id)
youtube_ids = []
for track in tracks:
    youtube_ids.append(youtube.youtube_search(track))

youtube.youtube_to_mp3(youtube_ids)
move_mp3_to_music()
print('Passed:',youtube.passed)
