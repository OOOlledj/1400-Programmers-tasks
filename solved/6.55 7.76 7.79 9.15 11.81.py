import math
import random

def task_6_55(x=12444566666678,a=4,b=6):
    x  = str(x)
    ca = 0
    cb = 0
    for sym in x:
        if int(sym) == a:
            ca+= 1
        elif int(sym) == b:
            cb+= 1

    if ca < cb:
        sol = ' '
    else:
        sol = ' не '
    print('Утверждение, что цифра а встречается реже чем b{}верно'.format(sol))

def task_7_76():
    '''[n team,time]'''
    rems = []
    for i in range(24):
        rems.append([random.randint(1,2),random.choice([2.5,10])])
    remtime1 = 0
    remcoun1 = 0
    remtime2 = 0
    remcoun2 = 0
    for rem in rems:
        if rem[0] == 1:
            remtime1+= rem[1]
            remcoun1+= 1
        elif rem[0] == 2:
            remtime2+= rem[1]
            remcoun2+= 1
    print('Команда {} удалялась {} раз, общее время удалений {}'.format(1, remcoun1, remtime1))
    print('Команда {} удалялась {} раз, общее время удалений {}'.format(2, remcoun2, remtime2))

def task_7_79(team = [3,3,1,1,0,0,1,3,1,0]):
    '''3/4/3'''
    lose = 0
    wins = 0
    draw = 0
    for i in team:
        if i == 3:
            wins+= 1
        elif i == 1:
            draw+= 1
        else:
            lose+= 1
    print('Итог команды: %i побед, %i в ничью, %i поражений' %(wins,draw,lose))

def task_9_15():
    shops = []
    for i in range(3):
        row = []
        for i in range(10):
            row.append(random.randint(1,100000))
        shops.append(row)
    for i in shops:
        print(i)

    for shop in shops:
        best = shop[0]
        day = 0
        i = 0
        while i < len(shop):
            if shop[i] > best:
                best = shop[i]
                day = i
            i+= 1
        print('Лучший день магазина',shops.index(shop)+1,':',day+1)

    i=0
    while i < 10:
        best = 0 #day
        shop = 0
        j = 0
        while j < 3:
            if best < shops[j][i]:
                best = shops[j][i]
                shop = j
            j+= 1
        print('Лучший магазин дня №%i:' %(i+1),shop+1)
        i+= 1

def task_11_81(arr = [1,4,8,16,91,5,16,14,78,9,12]):
    '''default: 4-8,8-16,16-14,14-78, it is 4'''
    l = len(arr) - 1
    i = 0
    pairs = 0
    while i < l:
        if arr[i]%2==0 and arr[i+1]%2==0:
            pairs+= 1
        i+= 1
    print('Число соседних четных пар чисел:',pairs)

task_11_81()