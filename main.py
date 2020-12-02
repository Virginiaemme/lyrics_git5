from music_package import lyrics as ly
from music_package import tabs as ta
import argparse
import os
import databmanager

def argparse(): #here we collect the inputs, the results will be organized in arrays and inserted in the url
    parser = argparse.ArgumentParser()
    parser.add_argument("artist", help="add artist")# nargs='+')
    parser.add_argument("title", help="add title", nargs='+')
    parser.add_argument('-v','--verbosity',help='increase output verbosity', action='store_true')
    args = parser.parse_args()
    return args



if __name__ == "__main__":
    ''' Execute code only if the file was run directly.'''
    databmanager.open_and_create('database.db')
    args = argparse
    if databmanager.check_user(args.usr, args.psw):
        ly.get_lyric(args.artist, args.title, args.verbosity)
        ta.get_tabs_id (args.artist)
    else:
        print('''
              Sorry, wrong username password selected!
              You may wanna register a new account through databmanager app.
              ''')