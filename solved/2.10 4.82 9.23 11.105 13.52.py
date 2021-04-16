import math
import random

def task_2_10(a,b):
    sa = (a+b)/2
    sg = math.sqrt(a*b)
    print('Среднее арифметическое и геометрическое:',sa,sg)

def task_4_82(age):
    if (20 >= age >= 11) or (9>=age%10>=5) or age%10==0:
        word = 'лет'
    elif age%10<5:
        word = 'год'
        if age%10!=1:
            word+='а'
    print('Мне',age,'{}'.format(word))
#for n in range(1,100):
    #task_4_82(n)

def task_9_23(a=17,b=128,k=5):

    def countdivs(n):
        s = 0
        for i in range(1,n+1):
            if n%i==0:
                s+=1
        return s

    for n in range(a,b+1):
        if countdivs(n)==k:
            print(n)

def task_11_105(arr=[]):
    if len(arr) == 0:
        for i in range(6):
            arr.append(random.randint(1,10))
        #print(arr)
    i=0
    flag = False
    while i < len(arr)-1:
        j = i+1
        while j < len(arr):
            #print(arr[i],arr[j])
            if arr[i]==arr[j]:
                flag= True
            j+= 1
        i+= 1
    print('Наличие в массиве одинаковых элементов:',flag)

def task_13_52():
    # bones1: 16,65,51,10,00,04,44 ok
    dominoleft = [1,6,5,1,0,0,4]
    dominorigh = [6,5,1,0,0,4,4]

    # bones2: 16,65,51,01,00,04,44 ok
    #dominoleft = [1,6,5,0,0,0,4]
    #dominorigh = [6,5,1,1,0,4,4]
    i = 0
    flag1 = False
    flag2 = False
    while i < len(dominorigh)-1:
        #1
        if dominorigh[i]==dominoleft[i+1]:
            pass
        else:
            if not flag1:
                bone1 = [dominoleft[i+1],dominorigh[i+1]]
                flag1 = True
                numb1 = i
        #2
        ll = dominoleft[i] == dominoleft[i + 1]
        lr = dominoleft[i] == dominorigh[i + 1]
        rl = dominorigh[i] == dominoleft[i + 1]
        rr = dominorigh[i] == dominorigh[i + 1]
        if ll or lr or rl or rr:
            pass
        else:
            if not flag2:
                bone2 = [dominoleft[i+1],dominorigh[i+1]]
                flag2 = True
                numb2 = i
        i+= 1
    print('Вариант 1:')
    if flag1:
        print('Кость, нарушающая правила: ',numb1+2,bone1)
    else:
        print('Кости разложены верно')
    print('Вариант 2:')
    if flag2:
        print('Кость, нарушающая правила: ',numb2+2,bone2)
    else:
        print('Кости разложены верно')



