from Player import Player
import random

def createCharacter():
    name = getName()
    stattuple = getStats()
    healthmod = stattuple[1]
    stats = stattuple[0]

    return Player(stats, name, healthmod)

def getName():
    input = raw_input("Name your hero: ")
    input = input.replace('=', '')
    if len(input) == 0:
        print "WE REQUIRE A NAME!"
        getName()
    return input

def getStats():
    points = 30
    stats = {'str': 1, 'dex': 1, 'end': 5, 'int': 3, 'res': 5, 'luc': 0}

    while True:
        print "\nYou have %d points remaining" % points
        printStats(stats)
        type = raw_input("Enter a stat, type \'random\', or type \'accept\': ")
        type = type[0:3].lower()
        if type in stats.keys():
            num = raw_input("Modify the value: ")
            try:
                num = int(num)

                if stats[type] + num < 0:
                    diff = abs(stats[type]+num)
                    num += diff
                elif num > points:
                    num = points
                stats[type] += num
                points -= num
            except:
                print "Not a number"
        elif type == 'acc':
            break
        elif type == 'ran':
            points = 30
            stats = {'str': 1, 'dex': 1, 'end': 5, 'int': 3, 'res': 5, 'luc': 0}
            l = stats.keys()
            while points > 0:
                choice = random.randint(0, len(l)-1)
                num = random.randint(1, 3)
                if num > points:
                    num = points
                stats[l[choice]] += num
                points -= num

                per = .25 ** (points/10.0)
                per *= 80
                v = random.randint(0, 100)
                if v < per:
                    break

        else:
            print "Not a valid option"

    healthmod = points

    return stats, healthmod


def printStats(stats):
    print "Strength: %d\nDexterity: %d\nEndurance: %d\nIntelligence: %d\nResistance: %d\nLuck: %d" % (stats['str'], stats['dex'], stats['end'], stats['int'], stats['res'], stats['luc'])
    print