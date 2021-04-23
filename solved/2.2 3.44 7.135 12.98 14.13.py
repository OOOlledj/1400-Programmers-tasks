import math
import random

def task_2_2(a):
    f = (a**2 + 10)/(math.sqrt(a**2 + 1))
    print('f(%f)=%f' %(a,f))

def task_3_44(a3=3,a2=2,a1=1,b2=4,b1=5):
    ab = a3*100 + 10*(a2+b2) + a1 + b1
    c4 = int(ab / 1000)
    c3 = int((ab%1000)/100)
    c2 = int((ab%100)/10)
    c1 = int(ab%10)
    print(c4,c3,c2,c1)

def task_7_135():
    arr = []
    for i in range(15):
        next = random.random()*random.randint(1,10)
        arr.append(next)
    print(arr)
    mn = arr[0]
    mx = arr[0]
    for next in arr:
        if next > mx:
            mx = next
        if next < mn:
            mn = next
    print('Min: %f, Max:%f' %(mn,mx))

def task_12_98(se = "небольшое предложение"):
    su = ''
    for char in se:
        if char == 'е':
            su+= 'и'
        else:
            su+= char
    print(su)

def task_14_13():

    def sign(a):
        if a < 0:
            return -1
        elif a == 0:
            return 0
        else:
            return 1
    try:
        x = float(input('x:'))
        y = float(input('y:'))
    except ValueError:
        print('incorrect input')
        return
    z = sign(x) + sign(y)
    print(z)

task_14_13()