# Organ Entrails
Console text-based "Choose Your Own Adventure" style game based on Oregon Trail and Zombies.
Written in Python to help teach the Programming Merit Badge

##Installation Instructions:

###Prerequisites
1 - You will need a copy of the Python SDK. This is not standard in all operating systems, so download and install here:
    https://www.python.org/downloads/
    It was written for Python 2.7, but feel free to fork the code and port to 3 if you like.

2 - You need to clone this repository. If you don't have git installed, download here:
    https://git-scm.com/downloads

###Install
Once you have the prerequisites installed (or are just using a Raspberry Pi) clone this repo by typing in your console:

git clone https://github.com/3leftturns/organ_entrails.git

This will download the code to your current folder.

type

cd src/game

to access the game.

then type

python organ_entrails.py

and the game will run. Follow the on screen helps to play. Send any feedback to github@andrewtjohnson.me


###Updating the repository

You will need to fork this repository to your own repo. To do this, click the fork button on the right, and choose your own repository.

Then use git clone to pull down the fork to your working directory.

git clone <the url of your fork>

Open the file in a text editor (notepad for windows is fine, Notepad++ is a little better; textedit for Mac, or Sublime text is a good choice too.)
* Using a document editor like MS Word will NOT work *

Test your changes by running the python file using

python organ_entrails.py

as a terminal command in the console. Once it works, you need to commit the changes to git.

First, commit the changes locally:

git status
(this will tell you the status of the changes)

git add -A
(this adds all changed files to the repo)

git status
(again to verify your changes are now staged for commit)

git commit -m 'put a message between the quotes here with your changes'
(commits to this repo will require a commit message)

At this point everything is up to date locally. Now we need to push it to the cloud:

git push

*The current release of this code is in Alpha and has known bugs and is not optimized.*