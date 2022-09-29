import random, sys, os, time
import termios
import fcntl
import os
import getch
import util

kb = util.KBHit()

def p(x, y): return (x, y) #direction
def r_int16(): return random.randint(0, 15) #random a int
def r_int32(): return random.randint(0, 31) #random a int
def hself(p): return s.count(p) == 1 #hit self, return true if p in s
def hwall(h): return h[0] < 0 or h[0] > 31 or h[1] < 0 or h[1] > 15 #hit boundry, return true if h is hit / out of bound
def r_food(): #random a food
    f = (r_int32(), r_int16())
    if not hself(f): return f
    else: return r_food()
def move(h, d): return (h[0]+d[0], h[1]+d[1]) #move towards to direction
def eat(h, f): return h[0] == f[0] and h[1] == f[1] #eat? return true if eatern
def canvas(): #draw
    stage = [['-']*16]*32
    for y in range(0, 16):
        for x in range(0, 32):
            if hself((x, y)): #or (f[0] == x and f[1] == y):
                stage[x][y] = 'O'
            elif f[0] == x and f[1] == y:
                stage[x][y] = '*'
            else:
                stage[x][y] = '-'
            sys.stdout.write(str(stage[x][y]))
        sys.stdout.write('\n')
def key_listen():
    #windows
    #key = msvcrt.getch()
    key = kb.getch()
    #key = kb.getarrow()
    #key = getch.getch()
    #print("keyl")
    if key in ['w', 'H', 0]: return (0, -1)
    elif key in ['s', 'P', 2]: return (0, 1)
    elif key in ['a', 'K', 3]: return (-1, 0)
    elif key in ['d', 'M', 1]: return (1, 0)
    else: return False

s = [(8,0),(7,0),(6,0),(5,0)]
d = p(1, 0)
f = r_food()
while 1:
    #windows
    #if msvcrt.kbhit():
    if kb.kbhit():
        tempd = key_listen()
        if tempd and (tempd[0]+d[0] != 0) and (tempd[1]+d[1] != 0):
            d = tempd
    new_head = move(s[0], d)
    if hself(new_head) or hwall(new_head):
        print('--Game Over--\nYour score is:' + str(len(s) - 4))
        break
    os.system('clear')
    s.insert(0, new_head)
    if eat(s[0], f):
        f = False
    else:
        s.pop()
    if not f: f = r_food()
    canvas()
    time.sleep(0.3)


