import math
import random

def task_1_16(t,v,x,y):
     print('\n5 7\n7 cm')
     print('\n100 {}\n1949 {}'.format(t,v))
     print('\n{} 25\n{} {}'.format(x,x,y))

def task_10_6():
    arr = []
    for i in range(50):
        arr.append(random.choice((0,1)))
    cnt1 = 0
    cnt0 = 0
    for i in arr:
        if i == 1:
            cnt1+= 1
        elif i == 0:
            cnt0+= 1
    print('Нулей: %i, единиц: %i' %(cnt0,cnt1))

def task_11_183():
    citys = []
    for i in range(29):
        citys.append(random.randint(50,1500))
    citys.sort()
    ordcity = random.randint(50,1500)
    print(citys,ordcity)
    for i in range(29):
        if citys[i] > ordcity:
            citys.insert(i,ordcity)
            break
    print(citys)

def task_12_129(text,sym,n):
    text+= '_'
    text = text[0:n-1] + sym + text[n-1:len(text)-1]
    print(text)
#task_12_129('Writeline','A',4)

def task_12_150(text):
    s = 0
    maxc = None
    firstone = True
    for sym in text:
        if sym in '0123456789':
            s+= int(sym)
            if firstone:
                firstone = False
                maxc = int(sym)
            else:
                if maxc < int(sym):
                    maxc = int(sym)
    print('Сумма цифр в строке: %i, наибольшая цифра:' %s,maxc)
