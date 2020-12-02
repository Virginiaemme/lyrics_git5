import requests
import json

def get_tabs_id(artist):

    """  The function returns the guitar tabs of a song. """

    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + artist)

    data = json.loads(r.text)

    return ('In order to get tabs of the song you have to put in the following link the ID of your song and google it.',
    '\n You can find the ID of the songs in the below database. \n\n',
    'LINK: http://www.songsterr.com/a/wa/song?id=', '\n\n', data)
