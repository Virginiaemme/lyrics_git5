from music_package import lyrics as ly
from music_package import tabs as ta
import argparse as arg
import os
import databmanager
import sys

def argparse(): #here we collect the inputs, the results will be organized in arrays and inserted in the url
    parser = arg.ArgumentParser()
    parser.add_argument(
        "artist", 
        help="add artist between double quotes")
    parser.add_argument(
        "title", 
        help="add title between double quotes")
    parser.add_argument(
        '-v','--verbosity',
        help='increase output verbosity', 
        action='store_true')
    parser.add_argument(
        '-usr',
        help="Write your username here",
        required=True)
    parser.add_argument(
        '-psw',
        help="Write your password here",
        required=True)
    args = parser.parse_args()
    return args
    
if __name__ == "__main__":
   
    ''' Execute code only if the file was run directly.'''
    
    databmanager.open_and_create('database.db')
    args = argparse()
    if databmanager.check_user(args.usr, args.psw):
        song_lyrics = ly.get_lyric(args.artist, args.title, args.verbosity)
        song_tabs = ta.get_tabs_id (args.artist)
        print(song_lyrics, song_tabs)
    else:
        print('''
              Sorry, wrong username password selected!
              You may wanna register a new account through databmanager app.
              ''')
