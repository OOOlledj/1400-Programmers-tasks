import math
import random

def task_2_31(x,y,z,
              candy=440,cookie=311,apple=89):
    s = x*candy +\
        y*cookie +\
        z*apple
    print('Сумма покупки:',s)

def task_6_13():
    i = 10
    while i <= 30:
        print(i)

    #нет постусловия

def task_6_49(N):

    n = []
    while N > 0:
        n.append(N%10)
        N = int(N/10)
    n.reverse()

    a = sum(n) > 10
    b = 1
    for i in n:
        b*= i
    b = b < 50
    v = len(n) % 2 == 0
    g = len(n) == 4
    d = n[0] <= 6
    e = n[0] == n[len(n)-1]
    j = n[0] >= n[len(n)-1]
    print('Сумма цифр больше 10:',a)
    print('Произведение цифр меньше 50:', b)
    print('Количество цифр четное:', v)
    print('Число четырехзначное:', g)
    print('Первая цифра не превышает 6:', d)
    print('Начинается и заканчивается одной цифрой:', e)
    if j:
        j = 'первая'
    else :
        j = 'вторая'
    print('Большая цифра из первой и последней:',j)

def task_8_1(n):
    i = 1
    while True:
        if i**2 <= n:
            print(i**2,end=' ')
        else:
            break
        i+= 1

def task_13_30():

    items = []
    for i in range(30):
        m = random.random() * random.randint(1,100)
        v = random.random()
        items.append([m,v])
    i = 0
    order = 0
    minp = items[0][0]/items[0][1]
    while i < 30:
        next = items[i][0]/items[i][1]
        if next < minp:
            minp = next
            order = i
        i+= 1
    print('Вещество с наименьшей плотностью:',order,'(%f) kg/m^3' %minp)

task_13_30()

