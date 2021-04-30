import math
import random

def task_3_1(cm):
    m = int(cm/100)
    print('Полных метров:',m)

def task_4_99(a,b):
    #1
    if a>=b:
        big=a
    if b>=a:
        big=b
    print('1.Наибольшее число:', big)
    #2
    big = a
    if a<=b:
        big=b
    print('2.Наибольшее число:',big)

def task_7_19():
    feb = []
    for i in range(28):
        feb.append(random.randint(0,40))
    pre = random.random()*28*25
    ths = 0
    for day in feb:
        ths+= day
    word = ' '
    if pre >= ths:
        word = ' не '
    else:
        pass
    print("Осадки в феврале этого года"+word+"превысили показатели за прошлый год")

def task_12_1():
    fname = input('Ваше имя:')
    sname = input('Ваша фамилия:')
    name = fname + ' ' + sname
    print('Вас зовут',name)

def task_13_1():
    fnames = []
    snames = []
    for i in range(25):
        fnames.append('fname' + str(i) + '-' + str(random.randint(100,999)))
        snames.append('sname' + str(i) + '-' + str(random.randint(100, 999)))
    i = 0
    while i < 25:
        print(fnames[i],snames[i])
        i+= 1
task_13_1()