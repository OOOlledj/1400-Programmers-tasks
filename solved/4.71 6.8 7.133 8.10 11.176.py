import math
import random

def task_4_71(v0=120,A=45,R=1400,H=50,p=25):
    x = R
    a = A * math.pi /180
    t = x/(v0 * math.cos(a))
    y = v0 * t * math.sin(a) - (9.8*(t**2))/2
    print('Угол запуска %f, начальная скорость %f, время до цели: %f' %(A,v0,t))
    print('Снаряд пролетает на высоте',y)
    if y >= H and y <= H+p:
        print('Попадание')
    else:
        print('Промах')

def task_6_8(n):
    for i in range(100):
        if i**2 <= n:
            pass
        else:
            print('Это число:',i)
            break

def task_7_133(seq = [1.1,2.2,3.3,3.3,3.3,15.2,9,8,1000]):
    l = len(seq)-1
    i = 0
    ct = 1
    fl = True
    while i < l:
        if seq[i]==seq[i+1] and fl:
            ct+= 1
        else:
            if ct==1:
                pass
            else:
                fl = False
        i+= 1
    print('Количество идущих подряд равных чисел:',ct)

def task_8_10(a):
    for i in range(1,25):
        number = 1+1/i if i!=1 else 1
        if a > number:
            print(number)

def task_11_176(arr = [1,2,3,4,5,6,7,8]):
    l = len(arr)-1
    buff = arr[0]
    i = 0
    while i < l:
        arr[i] = arr[i+1]
        i+=1
    arr[l] = buff
    print(arr)
