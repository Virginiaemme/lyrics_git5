import requests
import json

""" 

The function returns the lyrics of a song given the title and the artist.
    
    :param artist: artist name
    :type artist: string
    :param title: title of the song
    :type title: string

"""

SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'


def get_lyric( artist, title):

    URL = SONG_URL.format(artist, title)

    r = requests.get(URL)
    data = json.loads(r.text)

    try:
        song = data['lyrics']
    except TypeError:
        pass

    return song



""" 

The function returns the guitar tabs of a song.

"""


def get_tabs_id():

    Artist = input("Please enter the Artist whose song you are looking for: ")

    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + Artist)

    my_dict = r.json()

    return(my_dict, 'You will find the tabs of the song by googling http://www.songsterr.com/a/wa/song?id= and add the id of the song you want' )

