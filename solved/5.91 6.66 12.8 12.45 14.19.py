import math
import random

def task_5_91(n=260,D=50):
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    b = 0
    v = 0
    g = len(a)
    d = 0
    e = 0
    j = 0
    for i in a:
        b+= i
        if i % 2 == 0:
            v+= i
            e+= 1
        else:
            d+= 1
        if i > D:
            j+= 1
    print('а) Делители:',a)
    print('б) Сумма делителей:',b)
    print('в) Сумма четных делителей:',v)
    print('г) Количество делителей:',g)
    print('д) Количество нечетных делителей:',d)
    print('е) Количество четных делителей:',e)
    print('ж) Количество делителей, больших %i:' %D, j)

def task_6_66(a,b):
    #a,b = max(a,b), min(a,b)
    ans = 1
    while True:
        c = max(a,b)-min(a,b)
        print('%i - %i = %i' %(max(a,b),min(a,b),c))
        if c == 0:
           ans = max(a,b)
           break
        else:
            a = max(min(a,b),c)
            b = min(min(a,b),c)
    print(ans)
'''
task_6_66(96,128)
task_6_66(60,36)
task_6_66(37,17)
'''

def task_12_8(c1,c2,c3):
    if len(c1) > len(c2) and len(c1) > len(c3):
        maxc = c1
    elif len(c2) > len(c1) and len(c2) > len(c3):
        maxc = c2
    else:
        maxc = c3
    if len(c1) < len(c2) and len(c1) < len(c3):
        minc = c1
    elif len(c2) < len(c1) and len(c2) < len(c3):
        minc = c2
    else:
        minc = c3
    print(maxc,minc)

def task_12_45(char='#',n=10):
    s = char*n
    print(s)
    return s

def task_14_19():

    def filler():
        c = []
        for i in range(8):
            c.append(random.randint(1,10))
        return c

    a = filler()
    b = filler()

    def countodd(c):
        odd = 0
        for n in c:
            if n % 2 == 0:
                odd+= 1
        return odd

    odda = countodd(a)
    oddb = 8 - countodd(b)
    #print(a)
    #print(b)
    print('Четных чисел в 1-м массиве:', odda)
    print('Нечетных чисел в 2-м массиве:', oddb)
