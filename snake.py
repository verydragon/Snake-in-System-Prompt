import random, sys, os, time, msvcrt
def p(x, y): return (x, y) #direction
def r_int(): return random.randint(0, 15) #random a int
def hself(p): return s.count(p) == 1 #hit self, return true if p in s
def hwall(h): return h[0] < 0 or h[0] > 15 or h[1] < 0 or h[1] > 15 #hit boundry, return true if h is hit / out of bound
def r_food(): #random a food
    f = (r_int(), r_int())
    if not hself(f): return f
    else: return r_food()
def move(h, d): return (h[0]+d[0], h[1]+d[1]) #move towards to direction
def eat(h, f): return h[0] == f[0] and h[1] == f[1] #eat? return true if eatern
def canvas(): #draw
    stage = [['-']*16]*16
    for y in range(0, 16): 
        for x in range(0, 16):
            if hself((x, y)) or (f[0] == x and f[1] == y):
                stage[x][y] = 0
            else:
                stage[x][y] = '-'
            sys.stdout.write(str(stage[x][y]))
        sys.stdout.write('\n')
def key_listen():
    key = msvcrt.getch()
    if key in ['w', 'H']: return (0, -1)
    elif key in ['s', 'P']: return (0, 1)
    elif key in ['a', 'K']: return (-1, 0)
    elif key in ['d', 'M']: return (1, 0)
    else: return False
s = [(8,0),(7,0),(6,0),(5,0)]
d = p(1, 0)
f = r_food()
while 1:
    if msvcrt.kbhit():
        tempd = key_listen()
        if tempd and (tempd[0]+d[0] != 0) and (tempd[1]+d[1] != 0):
            d = tempd
    new_head = move(s[0], d)
    if hself(new_head) or hwall(new_head):
        print '--Game Over--\nYour score is:' + str(len(s) - 4)
        break
    os.system('cls')
    s.insert(0, new_head)
    if eat(s[0], f): 
        f = False
    else:
        s.pop()
    if not f: f = r_food()
    canvas()
    time.sleep(0.3)