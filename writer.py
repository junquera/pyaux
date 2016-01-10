import sys

def clear():
    sys.stdout.write(50*'\n')
    setPosition(0,0)

def setPosition(x,y):
    sys.stdout.write('\33[%d;%dH'%(x,y))
    sys.stdout.flush()

def write(x, y, text):
    setPosition(x,y)
    sys.stdout.write(str(text))
