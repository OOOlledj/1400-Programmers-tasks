import math
import random

def task_1_10():
    name = input('Ваше имя:')
    print('Вас зовут:',name)

def task_3_43(a1=3,a2=7,b1=5,b2=2):
    '''a1a2=37, b1b2=52, c1c2=89'''
    if (a1 + b1 > 9) or (a1 + b1 == 9 and a2 + b2 > 9):
        print('incorrect input')
        return
    c2 = (a2 + b2) % 10
    c1 = a1 + b1 + math.trunc((a2 + b2)/10)
    print('цифры получаемого числа:',c1,c2)

def task_11_34(arr = [-1.1,2.2,4.6,-29.14,0.98,-1.05,-8.752,14.6],k1=4,k2=2):
    arra = []
    arrb = []
    for i in arr:
        arra.append(i)
        arrb.append(i)
    l = len(arr)
    i = 0
    while i < l:
        if arra[i] > 0:
            arra[i]-= arra[k1]
        else:
            arra[i]-= arra[k2]
        if i%2!=0:
            arrb[i]+= 1.0
        else:
            arrb[i]-= 1.0
        i+= 1
    print(arr,'\n',arra,'\n',arrb)

def task_11_240():
    items = []
    for i in range(20):
        items.append([random.randint(1,10),random.randint(10,15000)])
    bestp = items[0][0]/items[0][1]
    bestn = 0
    i = 0
    while i < 20:
        newp = items[i][0] / items[i][1]
        if bestp < newp:
            bestp = newp
            bestn = i
        i+= 1
    print('Самое плоное вещество N%i - %f кг/см3' %(bestn,bestp))

def task_14_35(s1,s2):

    def countn(s):
        n = 0
        for char in s:
            if char == 'н':
                n+= 1
        return n

    print('Всего буков "н" в предложениях:',countn(s1)+countn(s2))
