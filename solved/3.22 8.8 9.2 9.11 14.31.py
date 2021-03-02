import math
import random

def task_3_22(xyz):
    yzx = int(xyz/100) + (xyz%100)*10
    print(yzx)
    
def task_8_8(a):
    n = 2
    while True:
        if (1+1/n > a):
            print(n, end = ' ')
            n+= 1
        else: break

def task_9_2():
    #a
    for i in range(1,10):
        for j in range(1,10):
            print(j,'+',i,'=',i+j,end='|')
        print()
    print()
    #b
    for i in range(1,10):
        for j in range(1,10):
            print(i,'+',j,'=',i+j,end='|')
        print()  

def task_9_11(months = 0):
    if (months==0):
        months = [[],[],[]]
        for mnt in range(3):
            for wrk in range(12):
                salary = random.randint(25000,55000)
                months[mnt].append(salary)
    else:
        pass
    print(months)
    print()
    #b
    for mnt in months:
        print(max(mnt),'is worker',
              mnt.index(max(mnt))+1)
    print()
    #a
    for i in range(12):
        m1,m2,m3=months[0][i], months[1][i], months[2][i]
        if m1>m2 and m1>m3:
            m=1
        elif m2>m1 and m2>m3:
            m=2
        else:
            m=3
        print('worker',i+1,'best month is N',m)
'''           
salrs = [[44468, 35427, 41968, 36822, 46486, 45181, 53009, 37531, 53512, 36977, 34211, 52129],
         [48782, 25510, 28416, 38812, 27762, 49016, 26494, 26553, 35220, 36608, 31029, 37472],
         [33264, 42022, 41677, 26873, 45502, 35115, 52317, 36366, 26405, 52827, 33325, 35539]]
task_9_11(salrs)'''

def task_14_31(a,b):
    q = [max(a,b),min(a,b)]
    while True:
        lft = q[0] % q[1]
        if lft == 0:
            NOD = q[1]
            break
        else:
            q = [min(a,b),lft]
    print('NOD',a,b,':',NOD)
    NOK = math.trunc(a*b/NOD)
    print('NOK',a,b,':',NOK)
    
task_14_31(30,18)
        