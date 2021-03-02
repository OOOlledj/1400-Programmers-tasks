import math
import random

def task_1_15():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print(a,b,c,d,sep=' ')
    
def task_6_41(n):
    arr = []
    while True:     
        if n==0:
            break
        step = n%10
        arr.append(step)
        n = int(n/10)
    print('max:',max(arr),'min:',min(arr))
        
def task_10_23():    
    nominal = ['шестерка', 'семерка', 'восьмерка', 
               'девятка', 'десятка', 'Валет', 
               'Дама', 'Король', 'Туз', ]
    crop = ['пик', 'крест', 'червей', 'бубен']
    lead = random.choice(crop)

    card = [random.choice(nominal),random.choice(crop)]
    card.append('козырь' if card[1]==lead else 'обычная')
    
    return card 

def task_12_41(s1):
    s2=''
    for l in range(len(s1)):
        if l%2 == 0 or l == 0:
            s2+=s1[l]
    print(s2)

def task_12_143():
    wordw = 'килбайот'
    #corr = 'килобайт'
    wordr = ''
    i=0
    flag=True
    while i < len(wordw):
        if i == 3 and flag:
            wordr+= wordw[6]
            i-= 1
            flag=False
        elif i == 6:
            pass
        else:
            wordr+= wordw[i]
        i+= 1
    print(wordr)