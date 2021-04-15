import math
import random

def task_5_24():
    i = 3.2
    while i < 4.0:
        print('%i,%i' %(math.trunc(i),math.trunc(i*10%10)))
        i+=0.1

def task_7_14(n=5):
    fl = []
    for i in range(n):
        fl.append(random.random()*10)
    s = 0
    for i in fl:
        s+= i**2
    print('Сумма квадратов вещественных чисел:',s)

def task_7_45():
    c = []
    for i in range(15):
        c.append(random.randint(1,25))
    s = 0
    print(c)
    for i in range(len(c)):
        if (i+1)%2!=0:
            s-= c[i]
    print(s)

def task_8_15(m=0.55):
    for x in range(1,100+1):
        y = (x**2+100)/(x+200)
        if y < m:
            print('x=%i:'%x,y)

def task_9_22():

    def countdivs(n):
        s = 0
        for i in range(1,n+1):
            if n%i==0:
                s+=1
        return s

    for num in range(200,500+1):
        if countdivs(num) == 6:
            print(num)

task_7_45()