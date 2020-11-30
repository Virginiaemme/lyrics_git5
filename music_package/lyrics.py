import requests
import json


SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'


def get_lyric( artist, title):

""" 

The function returns the lyrics of a song given the title and the artist.
    :param artist: artist name
    :type artist: string
    :param title: title of the song
    :type title: string

"""

    URL = SONG_URL.format(artist, title)

    r = requests.get(URL)
    data = json.loads(r.text)

    try:
        song = data['lyrics']
    except TypeError:
        pass

    return song