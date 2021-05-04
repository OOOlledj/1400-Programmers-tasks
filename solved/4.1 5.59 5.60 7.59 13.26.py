import math
import random

def task_4_1(a,b):
    if a > b:
        pass
    else:
        a,b=b,a
    print('%f is bigger than %f' %(a,b))

def task_5_59(n):
    f = 1
    i = 1
    while i <= n:
        f*= i
        i+= 1
    print('Факториал от n=%i: %i' %(n,f))

def task_5_60(n, a):
    s = 0
    i = 1
    while i <= n:
        s+= a
        i+= 1
    print('%i * %f = %f' %(n,a,s))

def task_7_59(n=20):
    cls = []
    for i in range(n):
        cls.append(random.randint(2,5))
    s = 0
    for mark in cls:
        if mark == 5:
            s+= 1
    print('Количество пятерок в классе: %i' %s)

def task_13_26():

    class vehicle:
        def __init__(self, type, price):
            self.type = type
            self.price = price
        def iscar(self):
            if self.type == 'car':
                return self.price
            else:
                return 0

    vehicles = []
    for i in range(15):
        type = random.choice(['car','truck'])
        price = 100000 * random.randint(8, 160)
        vl =  vehicle(type,price)
        vehicles.append(vl)
    s = 0
    for vl in vehicles:
        s+= vl.iscar()
    print('Общая стоимость легковых авто: %.1f' %s)
