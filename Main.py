import charactercreator as cc
import Commands
import IO
import os
from gamemap import gamemap

startingdir = os.getcwd()

player = None
m = None

exitgame = 0

def setup():
    if not os.path.exists(os.getcwd() + '/saves'):
        print "Creating saves folder"
        os.mkdir('saves')
    if not os.path.exists(os.getcwd()+'/maps'):
        print "Creating maps folder"
        os.mkdir('maps')


def main():
    setup()
    global player
    global m
    global exitgame
    while True:
        start = raw_input("Would you like to start a new game, load a game, delete a game, or quit? ")
        if start == 'new':
            new()
            break
        elif start == 'load':
            bool = load()
            if bool:
                break
        elif start == 'delete':
            delete()
        elif start == 'quit':
            exit(0)
        else:
            print "Invalid command, please try again."

    Commands.update(player, m)
    while True:
        m.printMap()
        Commands.getCommand()
        if exitgame == 1:
            exitgame = 0
            os.chdir(startingdir)
            main()
            break

def new():
    global player
    global m
    player = cc.createCharacter()
    m = gamemap()
    m.loadmap('start')

def load():
    global player
    global m
    name = raw_input("Enter the name of the character: ")
    os.chdir(startingdir + '/saves')

    if not os.path.exists(os.getcwd()+'/'+name):
        print "Not a valid file."
    else:
        res = IO.loadGame(name)
        if res is not None:
            player = res[0]
            m = res[1]
            return True
        else:
            return False

def delete():
    try:
        file = raw_input("Enter the name of the save: ")
        os.chdir(startingdir)
        os.remove('saves/'+file)
    except:
        print "File doesn't exist"

if __name__ == '__main__':
    main()







