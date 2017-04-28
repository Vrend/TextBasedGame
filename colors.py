def buildcolor(c, bc):
    dictc = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}
    dictbc = {'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47}

    if bc is None:
        return '\033[1;'+str(dictc[c])+'m'

    return '\033[1;'+str(dictc[c])+';'+str(dictbc[bc])+'m'


end = '\033[0m'


othergreen = '\033[0;32m'