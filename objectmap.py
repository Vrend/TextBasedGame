import colors as c

leger = {'dirt': c.buildcolor('red', None), 'tree': c.buildcolor('green', None), 'dense woods': c.othergreen}

def getobject(obj, keys, pos):
    if obj.strip() in keys.keys():
        obj = obj.strip()
        thing = keys[obj]
        res = leger[thing] + obj + c.end


        return res