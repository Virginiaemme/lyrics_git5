#! /usr/bin/env python3
'''
Database Manager module is used to manage user database operations.
dbmanager.py will enable you to:
- add a new account with username and password
- check if credentials inserted are present on the database
- remove an account from the database
The module is can be called directly to manage database or through the main file
 to check if the user is registered and allow the access.
Example:
    Adding a new user:
        $ python databmanager.py -usr test -psw test -add
            User [test] succesfully added to database!
    Removing a user:
        $ python databmanager.py -usr test -psw test -rm
            Successfully removed user [test]
    Checking credentials:
        $ python databmanager.py -usr test -psw test -check
            Credentials you have inserted for user [test] are the correct ones!
    Level of verbosity is regulated through the optional argument of the parser
.. 
'''

import sqlite3
import hashlib
import random
import os
from argparse import ArgumentParser

conn = None
cursor = None


def open_and_create(database):
    """Connect to the database or create a new one if it doesn't exist.
    Parameters:
        database (string): path to database
    """
    global conn
    global cursor
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        conn.commit()
    except sqlite3.OperationalError:
        cursor.execute('''CREATE TABLE users
                      (username CHAR(256) NOT NULL,
                       digest CHAR(256) NOT NULL,
                       salt SMALL INT NOT NULL,
                       PRIMARY KEY (username))''')


def parse_args():
    '''Command line option and argument parsing.
    The function use argparse to write user-friendly command-line interfaces.
    The argparse module also automatically generates help and usage messages
    and issues errors when users give the program invalid arguments.
    Arguments:
        ["-usr"] (required): Insert username of the account
        ["-psw"] (required): Insert password of the account
        ["-add"]: add a user
        ["-rm"]: remove a user
        ["-check"]: check a user
        ["--version"] (optional): show infos about the project
    Returns:
        argparse (namespace): user shell inputs arguments
    '''

    parser = ArgumentParser(
        description="Managing of the users database",
        prog="Eu",
        usage="%(prog)s [options]",
        epilog="Backend SQLite3")
    parser.add_argument(
        '-usr',
        help="Write your username here",
        required=True)
    parser.add_argument(
        '-psw',
        help="Write your password here",
        required=True)
    parser.add_argument(
        '-rm',
        help="Remove a user from the database",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        '-add',
        help="add a username",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        '-check',
        help="check if credentials are present in the database",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s v1.0, Dec 2019 by MFGAsoftware©")

    arguments = parser.parse_args()
    return arguments


def new_user(user, passw):
    """Register a new user.
    The SHA256, of salt plus password, is computed to obtain the digest.
    Password can so be stored in secure manner in encrypted version.
    Parameters:
        user (string): user username
        passw (string): user password
    """
    global conn
    global cursor
    sale = str(random.randint(1, 10000))
    digest = sale + passw
    for i in range(100000):
        digest = hashlib.sha256(passw.encode('utf-8')).hexdigest()
    row = cursor.execute("SELECT * FROM users WHERE username=?", (user,))
    results = row.fetchall()
    if results:
        print("Sorry, username [{}] is already in use. Please, retry!"
              .format(user))
        quit()
    else:
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                       (user, digest, sale))
        conn.commit()
        print("User [{}] succesfully added to database!".format(user))


def check_user(user, passw):
    """Check if credentials are correct.
    If the user exists the SHA256 is computed. Than, if the digest of the
    password provided by the user is the same as the digest computed as above,
    the user is authenticated and allowed to use functionalities.
    Parameters:
        user (string): user username
        passw (string): user password
    """
    global conn
    global cursor
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM users WHERE username=?",
                          (user,))
    results = rows.fetchall()
    conn.commit()
    if results == []:
        print('''
              Sorry, wrong username password selected!
              You may wanna register a new account through dbmanager app.
              ''')
        quit()
    password = str(results[0][2]) + passw
    digest = hashlib.sha256(passw.encode('utf-8')).hexdigest()
    if digest == results[0][1].lower():
        return True
    else:
        return False


def remove_user(user, passw):
    """Remove an old user.
    Parameters:
        user (string): user username
        passw (string): user password
    """
    global conn
    global cursor
    if check_user(user, passw):
        cursor.execute("DELETE FROM users WHERE username = ?", (user,))
        conn.commit()
        print("Successfully removed user [{}]".format(args.usr))
    else:
        print("Sorry, wrong or invalid password selected!")


if __name__ == "__main__":
    ''' Execute code only if the file was run directly.'''
    open_and_create('database.db')
    args = parse_args()
    bool1 = args.add and args.rm
    bool2 = args.add and args.check
    bool3 = args.rm and args.check
    if bool1 or bool2 or bool3:
        print("ATTENTION!! Can't execute both operations at the same time!")
        quit()
    if args.add:
        if args.usr is None or args.psw is None:
            print("Sorry, both username and password are required!")
        else:
            new_user(args.usr, args.psw)
    elif args.rm:
        remove_user(args.usr, args.psw)
    elif args.check:
        if check_user(args.usr, args.psw):
            print("Credentials for user [{}] are the correct ones!"
                  .format(args.usr))
        else:
            print("Sorry, wrong or invalid password selected!")
    else:
        print("Please select one operation [-add], [-rm] or [-check]!")
        conn.close()