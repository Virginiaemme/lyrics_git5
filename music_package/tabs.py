import requests
import json

def get_tabs_id(artist, verbosity=True):

def get_tabs_id(artist):

    """ 

    The function returns the guitar tabs of a song.

    """ 

    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + artist)
    
    data = json.loads(r.text)

    link = 'To get the tabs insert the ID of the song after this link: http://www.songsterr.com/a/wa/song?id= \n\n'
    b = 'Here you can find IDs of every song of {}, cheese the one that you are searching for here: \n\n {}'.format(artist,data)
    if verbosity:
    	return (link + b)
    else:   
    	return ("To get the tabs of the song insert the ID of the song in this link:  http://www.songsterr.com/a/wa/song?id=   ", data)
