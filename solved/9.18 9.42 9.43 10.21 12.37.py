import math
import random

def task_9_18():
    students = []
    for i in range(3):
        group = []
        for j in range(20):
            mark = []
            for k in range(3):
                mark.append(random.randint(2,5))
            group.append(mark)
        students.append(group)

    s1 = 0
    s2 = 0
    s3 = 0
    #i = 0
    for i in range(len(students)):
        for group in students[i]:
            for mark in group:
                if i == 0:
                    s1+= mark
                elif i == 1:
                    s2+= mark
                elif i == 2:
                    s3+= mark
    s1/= 60
    s2/= 60
    s3/= 60
    if s1 > s2 and s1 > s3:
        n = 1
        s = s1
    elif s2 > s1 and s2 > s3:
        n = 2
        s = s2
    else:
        n = 3
        s = s3
    print('Наивысший средний балл в группе №%i (%.3f)' %(n,s))

def task_9_42():
    for xyz in range(100,1000):
        st = str(xyz)
        if st[0]!=st[1] and st[0]!=st[2] and st[1]!=st[2]:
            print(xyz)

def task_9_43(n=[128,96,32]):

    def NOD2(a,b):
        while True:
            pNOD = min(a, b)
            left = max(a,b) % min(a,b)
            #print(a,b,left)
            if left == 0:
                return pNOD
            else:
                a, b = min(a,b), left

    i = 1
    cNOD = 1
    while i < len(n):
        if i == 1:
            cNOD = NOD2(n[i-1],n[i])
        else:
            cNOD = NOD2(cNOD,n[i])
        i+= 1
    print(cNOD)

def task_10_21():

    nominal = {6:'шестерка', 7:'семерка', 8:'восьмерка',
               9:'девятка', 10:'десятка', 11:'Валет',
               12:'Дама', 13:'Король', 14:'Туз'}
    n = range(6,14+1)
    crop = {1:'пик', 2:'крест', 4:'червей', 3:'бубен'}
    c = range(1,4+1)

    def getcard():
        return [random.choice(n),random.choice(c)]

    card1 = getcard()
    card2 = getcard()
    while True: #защита от генерации двух одинаковых карт
        if card2 == card1:
            card2 = getcard()
        else:
            break

    eld = 1
    yng = 2
    if card1[1] > card2[1]:
        pass
    elif card1[1] < card2[1]:
        eld, yng = 2, 1
    else:
        if card1[0] > card2[0]:
            pass
        else:
            eld, yng = 2, 1
    word = 'старше'
    if eld == 2:
        word = 'младше'
    print('карта игрока 1 {} карты игрока 2'.format(word), end=' (')
    print(nominal[card1[0]],crop[card1[1]],'и',nominal[card2[0]],crop[card2[1]],end = ')')


def task_12_37(w = 'creativity'):
    #1
    w1 = w[len(w)-3:len(w)] + w[3:len(w)-3] + w[0:3]
    print(w1)
    #2
    i = 0
    bfleft = ''
    bfright = ''
    while i < 3:
        righ = w[len(w) - (3 - i)]
        left = w[i]
        w = w[:i] + righ + w[i + 1:]
        w = w[:len(w) - (3 - i)] + left + w[len(w) - (3 - i) + 1:]
        i+= 1
    print(w)
