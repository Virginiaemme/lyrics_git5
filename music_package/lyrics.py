import requests
import json

def get_lyric( artist, title, verbosity=True):
    """The function returns the lyrics of a song given the title and the artist.
    
    :param artist: artist name
    :type artist: string
    :param title: title of the song
    :type title: string
    :param verbosity: verbosity activated 
    :type verbosity: bool
    :param SONG_URL: generic URL that will be implemented with input artist and title
    :type SONG_URL: string
    :return: lyrics of the chosen song 
    :rtype: string 
    
    """
   
    SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'
    URL = SONG_URL.format(artist, title)
    r = requests.get(URL)
    data = json.loads(r.text)
    try:
        song = data['lyrics']
    except TypeError:
        pass   
    if verbosity:
        return ('The song {} is from the artist {} and the lyrics is:\n\n{}'.format(title, artist, song))
    else:
        return song