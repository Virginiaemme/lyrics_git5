import requests
import json

def get_tabs_id(artist):
    """ The function returns the guitar tabs of a song.

    :param artist: artist name
    :type artist: string
    :return: all the artist's songs information, the user have to pick the ID of the choosen song to insert in the provided link
    :rtype: string
    """
    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + artist)
    data = json.loads(r.text)
    return ("To get the tabs of the song insert the ID of the song in this link:  http://www.songsterr.com/a/wa/song?id=   ", data)