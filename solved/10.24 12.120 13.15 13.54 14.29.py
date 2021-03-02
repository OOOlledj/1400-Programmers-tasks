import math
import random

def task_10_24():
    
    def randpos():
        return random.randint(1,8), random.randint(1,8)
    
    a, b = randpos()
    print('figure pos: ',(a,b))
    
    #task a
    while True:
        c,d = randpos()
        if (a!=c and b!=d):
            break
    print('ладья не угрожает ',(c,d))
    
    #taks b
    while True:
        c,d = randpos()
        if ((a-c != b-d) and (a+b != c+d)):
            break
    print('слон не угрожает ',(c,d))
    
    #task c
    while True:
        c,d = randpos()
        if (abs(a-c)<=1 and abs(d-b)<=1):
            break
    print('король одним ходом будет на поле ',(c,d))
    
    #task d
    while True:
        c,d = randpos()
        if (a!=c and b!=d) and ((a-c != b-d) and (a+b != c+d)):
            break
    print('Ферзь не угрожает полю ',(c,d))

def task_12_120():
     st = 'This is default string for any1 who want to read it'
     
     def generator(st):
         n1 = random.randint(0,len(st)-1)
         n2 = 0
         while n2 < n1:
             n2 = random.randint(0,len(st)-1)
         return n1, n2
     
     n1,n2 = generator(st)
     
     rst = st[0:n1] + st[n2:len(st)]
     print(st)
     print(rst)
     print(n1,n2)

def task_13_15():
    wAdd = {
        'Кузин': 'adress 1',
        'Кульков': 'adress 2',
        'Иванов': 'adress 3',
        'Кубиков':'adress 4',
        'Петров':'adress 5'
        }
             
    need = ['Кузин','Кульков','Кубиков']
    for i in need:
        print(i,wAdd[i])  
    
def task_13_54(defin):
    chem = {
        'H':'Hydrogen',
        'Li':'Lithium',
        'Na':'Natrium',
        'Ca':'Calcium'
        }
    
    print(chem.get(defin))
    
def task_14_29():
    
    def filler(n):
        arr1, arr2, arr3 = [],[],[]
        for i in range (n):
            arr1.append(random.randint(0,14))
            arr2.append(random.randint(0,14))
            arr3.append(random.randint(0,14))
        return arr1, arr2, arr3
    
    n = 15
    arr1, arr2, arr3 = filler(n)
    n1, n2, n3 = 0,0,0
    
    print(arr1)
    print(arr2)
    print(arr3)
    
    def cutter(arr):
        arrCut = []
        for i in arr:
            if i not in arrCut:
                arrCut.append(i)
        return arrCut
                
    arr1 = cutter(arr1)
    arr2 = cutter(arr2)
    arr3 = cutter(arr3)
    
    print(arr1)
    print(arr2)
    print(arr3)
    
    for i in arr3:
        if i in arr1:
            n1+=1
        if i in arr2:
            n2+=1    
    
    if n1 > n2:
        print('in arr 1 nums more')
    elif n2 > n1:
        print('in arr 2 nums more')
    else:
        print('the same count!')
    
    
#task_10_24()

#task_12_120()

#task_13_15()

'''task_13_54('Na')
task_13_54('Ca')
task_13_54('H')'''

#task_14_29()