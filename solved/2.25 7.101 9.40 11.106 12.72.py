import math
import random

def task_2_25(a,b,c):
    Sbok = 2*c*(a+b)
    V = a*b*c
    print('Площадь боковой поверхности:',Sbok)
    print('Объем',V)

def task_7_101(seq = []):
    if seq == []:
        for i in range(10):
            seq.append(random.random()*100)
    seq.append(10000)
    flag = True
    posf = 1
    for i in range(1,len(seq)):
        if seq[i] < seq[i-1]:
            posf = i
            flag = False
            break
    #print(seq)
    if flag:
        print('Последовательность возрастающая')
    else:
        print('Первый элемент, нарушающий последовательность №',posf)

def task_9_40(n):
    s = 0
    i = 1
    while i <= n:
        s+= i**i
        i+= 1
    print(s)

def task_11_106(seq = [1,2,3,3,4,5]):
    if seq == []:
        for i in range(10):
            seq.append(random.randint(1,10))

    cnt = []
    for i in range(len(seq)):
        n = i
        counter = 0
        for j in range(n,len(seq)):
            if seq[i] == seq[j]:
                counter+= 1
        cnt.append(counter)

    flag = False
    alrd = False #mens 'alredy have flag=True'
    for i in cnt:
        if i == 2 and not alrd:
            flag = True
            alrd = True
        elif i == 3: #if have more than 2 times of one element
            flag = False
            alrd = True

    #print(seq)
    #print(cnt)
    if flag:
        print('OK')
    else:
        print('not ok')

def task_12_72(st = 'some text with couple of movings'):
    c = 0
    m = 0
    i = 0
    while i < len(st):
        if st[i].lower() == 'c':
            c = i
        elif st[i].lower() == 'm':
            m = i
        i+= 1
    phrase = 'встречается позже'
    if c > m:
        print('"c"',phrase,'"m"')
    else:
        print('"m"',phrase,'"c"')
