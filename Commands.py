import IO
import sys

Main = sys.modules['__main__']

player = None
m = None

def update(pl, ma):
    global player
    global m
    player = pl
    m = ma

def getCommand():
    commands = {'n': north, 's': south, 'e': east, 'w': west, '?': hlp, 'help': hlp, 'save': save, 'exit': exitgame, 'stats': stats}

    com = raw_input("Please enter a command: ")

    if com.lower() in commands.keys():
        commands[com]()
    else:
        print "Invalid command"

def stats():
    print
    st = player.stats
    print "Name: "+player.name
    print "Health: "+str(player.health)+' / '+str(player.maxhealth)
    print "Mana: "+str(player.mana)+' / '+str(player.maxmana)
    print "Carry Weight: "+str(player.currentweight)+' / '+str(player.weight)
    print "Stats: "
    for x in sorted(st.keys()):
        print x+": "+ str(st[x])

def hlp():
    print ""


def north():
    print "Moved North"


def south():
    print "Moved South"


def west():
    print "Moved West"


def east():
    print "Moved East"

def save():
    IO.saveGame(player, m)
    print "Game Saved"


def exitgame():
     Main.exitgame = 1