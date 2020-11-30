from music_package import lyrics.py
from music_package import tabs.py

def argparse(): #here we collect the inputs, the results will be organized in arrays and inserted in the url
    parser = argparse.ArgumentParser()
    parser.add_argument("artist", help="add artist")# nargs='+')
    parser.add_argument("title", help="add title", nargs='+')
    parser.add_argument('-v','--verbosity',help='increase output verbosity', action='store_true')
    args = parser.parse_args()
    return args
