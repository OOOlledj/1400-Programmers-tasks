import math
import random

def task_1_7():
    e = 2.71828
    print(format(e,'.1f'))

def task_2_33(x,y):
    avr = (x+y)/2
    print('средний возраст: %f' %(avr))
    xdif = abs(avr - x)
    ydif = abs(avr - y)
    print('Разница от среднего для Тани и Мити: %f, %f' %(xdif,ydif))

def task_9_28():

    def dividors(num):
        s = 0
        for i in range(1,num):
            if num % i == 0:
                s+= i
        return s

    for num in range(100,300):
        if dividors(num) == 50:
            print(num)

def task_11_87():
    arr = []
    for i in range(20):
        arr.append(random.randint(1,20))

    more10 = 0
    s = 0
    for j in arr:
        if j > 10:
            s+= j
            more10+= 1
    s/= more10
    print(arr)
    print('Среднее арифметическое чисел > 10: %f' %s)

def task_11_238():
    march = []
    janrr = []
    for i in range(31):
        march.append(random.randint(0,100))
        janrr.append(random.randint(0,100))
    maxmar = march[0]
    maxjan = march[0]
    for i in range(31):
        if march[i] > maxmar:
            maxmar = march[i]
        if janrr[i] > maxjan:
            maxjan = janrr[i]
    month = ('январе', 'марте')
    if maxmar > maxjan:
        month = month[1]
    else:
        month = month[0]
    print('Больше всего осадков выпало в %s' %month)

task_11_238()

