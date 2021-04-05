import math
import random

def task_1_14():
    x = int(input('Первое число:'))
    y = int(input('Второе число:'))
    z = int(input('Третье число:'))
    print('%i  %i  %i' %(x,y,z))

def task_3_24(xyz = 123):
    yxz = (int(xyz/100))*10 + (int(xyz%100/10))*100 + (xyz%10)
    print(yxz)

def task_9_4():
    marks = []
    i = 0
    while i < 12:
        student = []
        j = 0
        while j < 3:
            student.append(random.randint(2,5))
            j+= 1
        marks.append(student)
        i+= 1
    #
    i = 0
    while i < 12:
        m = marks[i]
        j = 0
        s = 0
        while j < 3:
            s+= m[j]
            j+= 1
        print('Сумма оценок ученика %i: %i' %(i+1,s))
        i+= 1

def task_11_125():
    hg = []
    for i in range(35):
        hg.append(random.randint(168,190))
    highest = hg[0]
    s = 0
    for ind in hg:
        if ind > highest:
            highest = ind
            s = 1
        elif ind == highest:
            s+= 1
    print("Людей наибольшего роста (%i): %i" %(highest,s))

def task_12_162(f = 12.345):
    f = str(f).split('.')
    lenint = len(f[0])
    lenflt = len(f[1])
    print('Длина целой части: {}'.format(lenint))
    print('Длина дробной части: {}'.format(lenflt))

task_12_162()