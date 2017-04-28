class Player(object):
    name = ''
    maxmana = 0
    maxhealth = 0
    health = 0
    mana = 0
    weight = 0
    currentweight = 0
    healthmod = 0

    stats = {'str': 0, 'dex': 0, 'end': 0, 'int': 0, 'res': 0, 'luc': 0}

    def __init__(self, stats, name, healthmod, currentweight=0, health=-1, mana=-1):
        self.name = name
        self.stats = stats
        self.maxhealth = (self.stats['str'] + self.stats['res']) * 2
        self.maxhealth += healthmod
        if health < 0:
            self.health = self.maxhealth
        else:
            self.health = health
        self.maxmana = self.stats['int'] * 3
        if mana < 0:
            self.mana = self.maxmana
        else:
            self.mana = mana
        if self.stats['str'] > self.stats['dex']:
            self.weight = (self.stats['end']+self.stats['str']) * 3
        else:
            self.weight = (self.stats['end']+self.stats['dex']) * 3
        self.currentweight = currentweight
        self.healthmod = healthmod

    def getHealth(self):
        return self.health

    def getMana(self):
        return self.mana

    def setHealth(self, num):
        self.health += num

        if self.health > self.maxhealth:
            self.health = self.maxhealth

        if self.health <= 0:
            return 1
        return 0

    def setMana(self, num):
        self.mana += num

        if self.mana > self.maxmana:
            self.mana = self.maxmana

        if self.mana < 0:
            self.mana += num
            return 1
        return 0

    def getStats(self):
        return self.stats

    def getWeight(self):
        return self.currentweight

    def setWeight(self, num):
        self.currentweight += num
        return 0