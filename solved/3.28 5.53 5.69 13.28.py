import random
import math

def task_3_28(n):
    '''xyzw'''
    #sub a
    a = (n % 10) *1000 + int((n%100)/10) *100 + int(n/100)%10 *10 + int(n/1000)
    print(a)
    #sub b
    inv = str(n)
    b = 1000*int(inv[1]) + 100*int(inv[0]) + 10*int(inv[3]) + int(inv[2])
    print(b)
    #sub c
    c = 1000*int(inv[0]) + 100*int(inv[2]) + 10*int(inv[1]) + int(inv[3])
    print(c)
    #sub d
    d1 = 1000*int(inv[2]) + 100*int(inv[3]) + 10*int(inv[0]) + int(inv[1])
    d2 = n%100 *100 + int(n/100)
    print(d1,d2)
    pass

def task_5_53():
    s=0
    for i in range(1,10):
        add = 2
        for j in range (i):
            add*=2
        s+= add
        print(add)
    print(s)
    

def task_5_69(n):
    
    def fact(n):
        st = 1
        if n == 0:
            return st
        for i in range(1,n+1):
            st*= i
        return st
    
    s=1
    for i in range(1,n+1):
        resfc = 1/fact(i)
        s+=resfc
    print(s)

def task_13_28():
    
    def create():
        return [random.randint(1,10),random.uniform(0.2,1.4)]
    
    arr = []
    for i in range(5):
        arr.append(create())
    
    maxp = 0
    index = 0
    for item in arr:
        nexp = item[0]/item[1]
        if nexp > maxp:
            maxp = nexp
            index = arr.index(item) + 1
    print('max P: ',maxp,' item № ',index)
    print(arr)
        

#task_3_28(1234)
#task_5_53()
#task_5_69(4)
#task_13_28()