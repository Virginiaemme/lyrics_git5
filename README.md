## GIT5: SONG LYRICS and TABS FETCHER PROJECT

Our project aims to grant users access to songs' lyrics and tabs through this simple tool that we created. 

### GETTING STARTED
The following guidelines will help final users to understand the whole project better and, of course, get a copy of our project and run it on their local machine for development and testing purposes.

### Repository structure

		music_package
						LICENSE.txt
						__init__.py
						lyrics.py
						tabs.py
		.gitignore
		README.rm
		database.db
		databmanager.py
		main.py


#### The package called ```music_package``` collect the following files:

- ```lyrics.py``` that query the [lyrics.ovh](https://lyricsovh.docs.apiary.io/#) website to fetch the lyrics of a song. It implements ```get_lyric( artist, title)``` function.

- ```tabs.py``` and [songsterr.com](http://www.songsterr.com/a/wa/song?id=) websites to fetch the songs' tabs. It implemnts ```get_tabs_id( artist)``` function.

- ```__init__.py``` file is required to make Python treat directories containing the file as packages: ignore it!

- ```LICENSE.txt``` file contain the chosen license for GIT5 project.

#### Other files in the repository:

- ```.gitignore``` file specifies intentionally untracked files that git should ignore.

- ```database.db``` file stores all usernames and encrypted passwords. Further information in the next section.

- ```databmanager``` file

- ```main.py``` file



### BEFORE STARTING: PREREQUISITES

1. Download of the repository from Git-hub [GIT5](https://github.com/Matteo-Cobian/lyrics_git5)

2. Check if all the needed libraries are installed.


:warning: The project requires the following modules to run:

 :warning: ```JSON``` , ```requests```, ```argparse```, ```sys``` , ```CSV```, ```os```, ```random```, ```hashlib``` modules. 

3. Use the command $ pip3 install libraryname to eventually install missing libraries.




	The system support a User Management System and so, you are going to need a valid username and password to login every time you execute the program.


### HANDS ON: POPULATE THE DB

4. Setup usernames and passwords, by executing databmanager.py from the command line.

		$ python databmanager.py -usr test -psw test -add/check/rm

	:warning: only one operation at time is supported.

#### How to:

- ADD a new user

		$ python databmanager.py -usr test -psw test -add
			User [test] added to database!	
	

- CHECK an existing user's credentials

		$ python databmanager.py -usr test -psw test -check
			Credentials for user [test] are the correct ones!


- REMOVE an old user

		$ python databmanager.py -usr test -psw test -rm
			The user [{}] has been removed.


All the users and their passwords are saved in the database.db file in the repository. The file is now empty. As soon as users add new usernames and passwords, they will be stored in there. For security reasons, it will not be possible to read passwords straightforward: they are stored as digest computed with a salt plus hash repetition.







If you run the program, executing the main file with: ```python main.py``` it will give you results similar to the following: 

CONTROLLARE QUESTO OUTPUT 

```
$ Python main.py
Across the Universe by Beatles:
Words are flowing out like 
Endless rain into a paper cup
They slither wildly as they slip away across the universe.
Pools of sorrow waves of joy
Are drifting through my opened mind
Possessing and caressing me.
...
```



A user can choose, ```title``` ( **Across the Universe** in the example) by the specified ```artist``` (**Beatles** in the example) to get the lyrics as output.

** AUTHENTICATION **

Descrizione divisione packages e moduli e aggiungerei anche 
The __init__.py files are required to make Python treat directories containing the file as packages: ignore it!


## DOCUMENTATION
Documentation is stored in the repository documentation. Please have a look to understand the functions of our modules better.



## TESTING

## SUPPORT

Do not hesitate if you need any support!

## AUTHORS AND ACKNOWLEDGMENT

- [Matteo Bianco](https://github.com/Matteo-Cobian)


- [Stefano Businaro](https://github.com/businer)


- [Divincenzo Francesco](https://github.com/divi999)


- [Grego Federico](https://github.com/Fede2302)


- [Virginia Massaccesi](https://github.com/Virginiaemme)


Also thanks to Prof. Pistellato and Prof. Maccari for their contribution.



## LICENSE
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)


