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
    if len (sys.argv)>3:
        print("you put more than three arguments or omit the "" when specifying the artist and song title")
    #the condition len(sys.arg)<3 is not needed, as the console autonomously gives an error if the number of arguments is less than 3 

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
