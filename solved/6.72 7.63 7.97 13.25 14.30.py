import math
import random

def task_6_72(f,s,n):
    #n = f + i*s, i E N
    res = ''
    if (n - f) % s == 0:
        pass
    else:
        res = 'не'
    print('n %s явлеяется членом арифметической прогрессии' %res)

def task_7_63():
    mrks = []
    for i in range(25):
        mrks.append(random.randint(2,5))
    res2 = 0
    res5 = 0
    for m in mrks:
        if m == 2:
            res2+= 1
        if m == 5:
            res5+= 1
    print('Двоек: %i\nПятерок: %i' %(res2,res5))

def task_7_97(seq = None):
    if seq == None:
        seq = []
        for i in range(random.randint(1,20)):
            seq.append(random.randint(-5,10))
    seq.append(-1)

    for i in range(1,len(seq)):
        if seq[i-1] == seq[i]:
            print('Есть пара соседних одинаковый чисел!')
            return
        else:
            pass
    print('Пары соседних одинаковых чисел нет')

def task_13_25():
    hght = []
    for i in range(22):
        hght.append(
            [random.randint(160,210),
             random.choice(['M','F'])]
        )
    mavr = 0
    mcnt = 0
    for person in hght:
        if person[1] == 'M':
            mavr+= person[0]
            mcnt+= 1
    mavr/= mcnt
    print('Средний рост мужчин: %i' %mavr)

def task_14_30(a,b):

    def ifpalindrome(x):
        x = str(x)
        palFlag = True
        while True:
            if x!= '' and int(x) > 9:
                #print(len(x)-1,x)
                if x[0] == x[len(x)-1]:
                    x = x[1:len(x)-1]
                else:
                    palFlag = False
                    break
            else:
                break
        return palFlag

    if ifpalindrome(a) and ifpalindrome(b):
        print('Хотя бы одно число - палиндром')
