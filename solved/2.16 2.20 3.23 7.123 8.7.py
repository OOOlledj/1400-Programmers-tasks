import math
import random

def task_2_16(a,b,c):
    return a+b+c

def task_2_20(f,g,h):
    a = math.sqrt(abs(math.e - 3/f)**3 + g)
    b = math.sin(math.e) + math.cos(h)**2
    c = (33*g) / (math.e*f - 3)

def task_3_23(xyz):
    z = xyz % 10
    zxy = z * 100 + math.trunc(xyz/10)
    return zxy

def task_7_123(hOne = 171):
    hg = []
    while len(hg) <= 15:
        addhg = random.randint(150,205)
        if addhg not in hg:
            hg.append(addhg)
    hg.sort(reverse=True)
    for i in range(len(hg)):
        if hg[i] < hOne:
            print('Он будет %i' %(i+1),'по росту')
            break

def task_8_7():
    while True:
        a = random.random() * 1.5
        if a > 1 and a <= 1.5:
            break
    print('a =',a)
    i = 2
    while True:
        step = (i+1) / i
        if step < a:
            print('Нашел! это %f' %(step), 'i = %i' %(i))
            break
        i+= 1