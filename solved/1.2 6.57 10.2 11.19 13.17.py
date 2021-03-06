import math
import random

def task_1_2():
    print("%i  %i  %i" %(47,52,150))

def task_3_20():
    xyz = random.choice(range(100,999))
    z = xyz % 10
    y = math.trunc((xyz % 100) / 10)
    x = math.trunc(xyz / 100)
    sxyz = x+y+z
    mxyz = x*y*z
    print('Number is:%i\nx=%i, y=%i, z=%i\nSum=%i\nMult=%i' % (xyz,x,y,z,sxyz,mxyz))

def task_10_2():
    a = []
    i = 0
    while i < 10:
        a.append(random.randint(0,10))
        i+= 1
    print('array a:',a)
    k = int(input('Put k:'))
    a = int(input('Put a:'))
    i = 0
    b = []
    while i < k:
        b.append(random.randint(0,a))
        i+= 1
    print('array b:',b)
    v=[]
    for i in range(20):
        v.append(random.randint(10,20))
    print('array v:',v)
    g = []
    for i in range(k):
        g.append(random.randint(-10,a))
    print('array g:',g)
    k = random.randint(0,15)
    a = int(input('Put a:'))
    b = int(input('Put b:'))
    d = []
    i = 0
    while i < k:
        d.append(random.randint(a,b))
        i+= 1
    print('k is %i and array d:' %(k),d)

def task_11_19():

    def isSimple(n):
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

    simplArr = []
    cNum = 100
    while len(simplArr) < 10:
        if isSimple(cNum):
            simplArr.append(cNum)
        else:
            pass
        cNum+= 1
    print(simplArr)

def task_13_17(name,numb):
    phbook = [
            ['ivanov',245617],['petrov',590404],['kabanova',113492],['klochkov',440917],['ivanko',171172],
            ['reznikova',138961],['stoleshnikov',876151],['kim',720103],['komarova',159091],['gusev',255670],
            ['serejkin',567219],['ramov',143469],['kramenko',513406],['dronov',901236],['lihacheva',152176]
              ]
    #search by name:
    for person in phbook:
        if name == person[0]:
            print(person)
    #search by number
    for person in phbook:
        if numb == person[1]:
            print(person)

