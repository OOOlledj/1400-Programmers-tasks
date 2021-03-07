import math
import random

def task_2_14(a,b):
    print(math.sqrt(a**2 + b**2))

def task_6_59(n):
    count = 0
    subs = n
    minn = 9
    while subs != 0:
        iter = subs % 10
        if iter < minn:
            minn = iter
        subs = math.trunc(subs/10)

    subs = n

    while subs !=0:
        iter = subs % 10
        if iter == minn:
            count+= 1
        subs = math.trunc(subs/10)
    print(count)

def task_6_80(N):
    i = 1
    Ns = str(N)
    incsec = True
    while i < len(Ns):
        if Ns[i-1] <= Ns[i]:
            pass
        else:
            incsec = False
        i+= 1
    if incsec:
        print('В порядке возрастания')
    else:
        print('Не в порядке возрастания')

def task_10_13(n=2):

    def cube():
        return random.randint(1,6)

    p1 = 0
    p2 = 0
    neutr = 0
    for i in range(n):
        c1 = cube()
        c2 = cube()
        if c1 > c2:
            p1+= 1
        elif c1 < c2:
            p2+= 1
        else:
            neutr+= 1
        print('game %i, results: %i and %i, count:%i-%i no-win: %i' %(i+1,c1,c2,p1,p2,neutr))

    win = 'Nobody'
    if p1 > p2:
        win = 'player 1'
    elif p2 > p1:
        win = 'player 2'
    print('%s won!' %(win))


def task_13_34():

    #create list of players
    chp = []
    for i in range(20):
        pers = ['player %i' %i,[]]
        for i in range(5):
            pers[1].append(random.randint(1,25))
        chp.append(pers)
    print("championship player's results:",chp)
    i = 1
    winner = chp[0]
    while i < 20:
        if sum(winner[1]) < sum(chp[i][1]):
            winner = chp[i]
            #print(winner, sum(chp[i][1]))
        i+= 1
    print('winner is',winner)


task_13_34()