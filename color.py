#make ANSI code for colours
def color(id):
        return u"\u001b[38;5;" + str(id) + "m"

#necessary colours
TITLE = color(220)
MANUAL = color(222)
REQUEST = color(157)
QUERY = color(155)
DATA = color(105)
MESSAGE = color(46)
ERROR = color(196)
ERRORINFO = color(124)
BULLET = color(224)
RESET = '\u001b[0m'