import math
import random

def task_4_6(x):

    def taska(x):
        if x < 2:
            y = x
        else:
            y = 2
        return y

    def taskb(x):
        if x > 3:
            y = -3
        else:
            y = -x
        return y

    print('y_a(x) =', taska(x))
    print('y_b(x) =', taskb(x))

def task_6_17():
    i = 1.0
    while i <= 13.5:
        print(i,end=' ')
        i+= 0.5

def task_6_29():
    i = 0
    num = 100
    while i < 10:
        if num % 10 == 7 and num % 9 == 0:
            i+= 1
            print(num, end=' ')
        num+= 1

def task_12_181(snt = 'welcome to the obviousland, re-evaluated sections'):
    alp = 'abcdefghijklmnopqrstuvwxyz '
    resnt = ''
    #normalize string
    for char in snt.lower():
        if char in alp:
            resnt+= char
        else:
            pass
    words = resnt.split(' ')
    print(words)

    def begincharend(word):
        if word[0] == word[len(word)-1]:
            return True
        else:
            return False

    def chare3(word):
        cnte = 0
        for char in word:
            if char == 'e':
                cnte+= 1
        if cnte == 3:
            return True
        else:
            return False

    def atl1o(word):
        if 'o' in word:
            return True
        else:
            return False

    a = []
    b = []
    c = []
    for word in words:
        if begincharend(word):
            a.append(word)
        if chare3(word):
            b.append(word)
        if atl1o(word):
            c.append(word)
    print('Начинаются и заканчиваются той же буквой: ',a)
    print('Имеют ровно 3 буквы "е":',b)
    print('Содержат хотя бы одну букву "о":',c)


def task_14_15(a1=4,b1=8,h1=4,a2=5,b2=2,h2=5):

    def ptrap(a,b,h):
        return a+b+2*math.sqrt(h**2 + (abs(a-b))**2/4)

    p = ptrap(a1,b1,h1) + ptrap(a2,b2,h2)
    print('Сумма периметров равнобедренных трапеций:',p)

task_14_15()

