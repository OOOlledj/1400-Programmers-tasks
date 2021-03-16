import math
import random

def task_4_39(t):
    signs = ('Зеленый', 'Красный')
    t = math.modf(t)
    t = t[0] + math.trunc(t[1])%60
    left = 0
    right = 3
    sign = signs[0]
    while left <= 60:
        if t <= right and t >= left:
            print('Светофор {}'.format(sign))
            break
        if (left + right) % 2 == 1:
            left+= 3
            right+= 2
            sign = signs[1]
        else:
            left+= 2
            right+= 3
            sign = signs[0]

def task_5_44(n):
    f1 = 1
    f2 = 1
    for i in range(3,n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if i == n:
            print('%i-е число Фибоначчи: %i' %(n,f3))
            break

def task_12_39(name):
    for sym in name:
        print(sym)

def task_12_79(phrase):
    i = 0
    first6 = 0
    word = ''
    while i < len(phrase):
        #print(i)
        if phrase[i] != ' ':
            word+= phrase[i]
        if phrase[i] == ' ' or i == len(phrase)-1:
            print(word)
            word = ''
            first6+= 1
        if first6 == 6:
            break
        i+= 1

def task_14_21(arra):
    n = len(arra)
    cnt = 0
    for a in arra:
        if math.modf(math.sqrt(a))[0] == 0:
            cnt+= 1
            print('Полный квадрат: %i' %a)
    print('Всего полных квадратов: %i' %cnt)
