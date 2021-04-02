import math
import random

def task_6_12():
    i = 0
    while True:
        num = int(input())
        if num!=0:
            print('Вы ввели число %i' %num)
        else:
            break

def task_9_21():

    def dividors(n):
        div = 0
        for i in range(1,n+1):
            if n%i==0:
                div+=1
        return div

    for i in range(1,300):
        if dividors(i) == 5:
            print(i)

def task_9_41(n=24):
    for i in range(100,1000):
        x = int(str(i)[0])
        y = int(str(i)[1])
        z = int(str(i)[2])
        if x+y+z == n:
            print(i)

def task_12_140(w='retrowave'):
    print(w[len(w)-1]+w[0:len(w)-1])

def task_13_20():
    cars = []
    for i in range(30):
        power = random.randint(80,280)
        costs = random.randint(500,3200) # *1000
        cars.append([power,costs])

    overall = 0
    for car in cars:
        if car[0] > 100:
            overall+= car[1]
    print('Общая стоимость машин с мощностью более 100 л.с.:',overall,'т.р.')

