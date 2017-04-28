import os
import objectmap as obj
import Main

class gamemap(object):
    mapset = []
    currentroom = None
    mapfolder = None
    keys = None
    x, y = 0, 0

    def loadmap(self, name, currentroom='00'):
        os.chdir(Main.startingdir)
        self.mapfolder = 'maps/'+name+'/'
        os.chdir(self.mapfolder)
        for filename in os.listdir(os.getcwd()):
            self.mapset.append(filename)
        if currentroom == '00':
            self.currentroom = self.mapset[0]
        else:
            self.currentroom = currentroom


    def printKey(self):
        if self.keys is not None:
            for x in self.keys.keys():
                print x + ' is ' + self.keys[x]

    def printMap(self):
        global x, y

        self.keys = {}
        print
        if self.currentroom is not None:
            os.chdir(Main.startingdir)
            os.chdir(self.mapfolder)
            file = open(self.currentroom, 'r')
            map = ''
            while True:
                line = file.readline()
                if not line == "\n":
                    map += line
                else:
                    break
            while True:
                line = file.readline()
                if not line == '':
                    if not line == '\n':
                        line = line.replace('\n', '')

                        if line.__contains__('start='):
                            line = line.replace('start=', '').strip()
                            x = int(line[0])
                            y = int(line[2])
                        else:
                            temp = line.split('=')
                            self.keys[temp[0]] = temp[1]
                else:
                    break
            map = self.colormap(map)
            print map
            self.printKey()
        else:
            print 'map not loaded'


    def colormap(self, map):
        lines = map.split('\n')
        lines.remove('')
        map = ''

        for x in range(0, len(lines)):
            line = ''
            chars = lines[x].split(' ')
            for y in range(0, len(chars)):
                val = chars[y]
                val = obj.getobject(val, self.keys, (x, y))
                line += val + ' '
            line = line.strip()
            line += '\n'
            map += line
        return map

