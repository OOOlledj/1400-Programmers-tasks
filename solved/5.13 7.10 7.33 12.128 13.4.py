import math
import random

def task_5_13():
    for i in range(1,10):
        print('%i x 7 =' %i, 7*i)

def task_7_10():

    def fillsport():
        s = []
        for i in range(5):
            s.append(random.randint(1,5))
        return s
    s1 = fillsport()
    s2 = fillsport()

    res1 = s1[0] + s1[1] + s1[2] + s1[3] + s1[4]
    res2 = s2[0] + s2[1] + s2[2] + s2[3] + s2[4]
    print('Спортсмен 1 получил очков:', res1)
    print('Спортсмен 2 получил очков:', res2)

def task_7_33():

    def rainmonth():
        month = []
        for i in range(30):
            month.append(random.randint(0,40))
        return month

    def getaver(month):
        s = 0
        for day in month:
            s+= day
        return s/len(month)

    jan = rainmonth()
    mar = rainmonth()
    aver1 = getaver(jan)
    aver2 = getaver(mar)

    print('Среднесуточные осадки в январе:', aver1)
    print('Среднесуточные осадки в марте:', aver2)

def task_12_128(k,word='schoolbus'):
    word+= '_'
    word = word[0:k]+'m'+word[k:len(word)]
    print(word)

def task_13_4():
    workers = []
    for i in range(16):
        age = random.randint(16,58)
        army = random.choice([True,False])
        workers.append([age,army])
    i = 0
    while i < len(workers):
        work = workers[i]
        if work[1]:
            print('Военнообязанный:',i,work)
        i+= 1
task_13_4()