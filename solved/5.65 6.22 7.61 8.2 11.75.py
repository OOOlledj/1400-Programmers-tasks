import math
import random

def task_5_65(x):
    y = 0
    for i in range(1,x+1):
        y+= 2*i - 1
    print('y(x) = x^2; y({})={}'.format(x,y))

def task_6_22(x=1529):
    while x >= 1000:
        x = math.trunc(x/10)
    print(x%10)

def task_7_61():
    jun = []
    for i in range(12):
        jun.append(random.randint(140,180))
    s = 0
    for i in jun:
        if i < 165:
            s+= 1
    print('Юношей ростом ниже 165: %i' %s)

def task_8_2(n):

    def result(i,n):
        print('%i^2 больше чем' % i, n)
    #1
    i = 1
    while True:
        if i**2 > n:
            result(i,n)
            break
        i+= 1
    #2
    i = 1
    while n > i**2:
        i+= 1
    result(i,n)

def task_11_75():
    matches = []
    for i in range(20):
        matches.append(random.choice([1,3,0]))
    wins = 0
    draw = 0
    for i in matches:
        if i==3: wins+= 1
        if i==0: draw+= 1
    print('Количество побед: %i\nКоличество ничейных матчей: %i' %(wins,draw))