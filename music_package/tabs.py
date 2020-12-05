import requests
import json

<<<<<<< HEAD
def get_tabs_id(artist, verbosity=True):
=======
def get_tabs_id(artist):
    """ The function returns the guitar tabs of a song.
>>>>>>> b9b269dd18c5c15228bf0f629fa05ab77a82b5b1

    :param artist: artist name
    :type artist: string
    :return: all the artist's songs information, the user have to pick the ID of the choosen song to insert in the provided link
    :rtype: string
    """
    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + artist)
    data = json.loads(r.text)
<<<<<<< HEAD
    link = 'To get the tabs insert the ID of the song after this link: http://www.songsterr.com/a/wa/song?id= \n\n'
    b = 'Here you can find IDs of every song of {}, cheese the one that you are searching for here: \n\n {}'.format(artist,data)
    if verbosity:
    	return (link + b)
    else:   
    	return ("To get the tabs of the song insert the ID of the song in this link:  http://www.songsterr.com/a/wa/song?id=   ", data)
=======
    return ("To get the tabs of the song insert the ID of the song in this link:  http://www.songsterr.com/a/wa/song?id=   ", data)
>>>>>>> b9b269dd18c5c15228bf0f629fa05ab77a82b5b1
