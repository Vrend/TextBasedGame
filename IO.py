import os
from Main import startingdir as sd
from Player import Player
from gamemap import gamemap

def saveGame(player, mapo):
    dir = 'saves/'
    os.chdir(sd)
    file = open(dir+player.name, 'w+')
    file.write('name='+player.name+'\n')
    file.write('health='+str(player.health)+'\n')
    file.write('healthmod='+str(player.healthmod)+'\n')
    file.write('mana='+str(player.mana)+'\n')
    file.write('currentweight='+str(player.currentweight)+"\n")
    file.write('stats='+str(player.stats)+'\n')
    file.write('map='+mapo.mapfolder+'\n')
    file.write('index='+mapo.currentroom+'\n')
    file.close()


def loadGame(name):
    os.chdir(sd)
    os.chdir('saves/')

    try:
        file = open(name, 'r')
        name = file.readline().replace('name=', '').strip()
        health = int(file.readline().replace('health=', '').strip())
        healthmod = int(file.readline().replace('healthmod=', '').strip())
        mana = int(file.readline().replace('mana=', '').strip())
        currentweight = int(file.readline().replace('currentweight=', '').strip())
        statsrough = file.readline().replace('stats=', '').strip()
        stats = {'str': 1, 'dex': 1, 'end': 5, 'int': 3, 'res': 5, 'luc': 0}
        for x in stats.keys():
            roughb = statsrough.find(x)
            roughe = statsrough.find(',', roughb, len(statsrough))
            if roughe == -1:
                roughe = statsrough.find('}', roughb, len(statsrough))
                if roughe == -1:
                    print "Problem"
            rough = statsrough[roughb:roughe]
            rough = rough.replace('\'', '')
            rough = rough.replace(':', '')
            rough = rough.replace(x, '')
            final = rough.strip()
            stats[x] = int(final)

        m = file.readline().replace('map=', '').strip()
        m = m.replace('maps/', '').replace('/', '').strip()
        index = file.readline().replace('index=', '').replace('maps/', '')
        index = index[0:len(index)-1]
        file.close()
        player = Player(stats, name, healthmod, currentweight, health, mana)
        ma = gamemap()
        ma.loadmap(m, currentroom=index)
        return player, ma
    except:
        print "File doesn't exist"
        return None
