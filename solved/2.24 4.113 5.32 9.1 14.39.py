import math
import random

def task_2_24(a,b):
    print(a,b)
    print('sum:{}'.format(a+b))
    print('dif:{}'.format(a - b))
    print('mul:{}'.format(a * b))
    print('div:{}'.format(a / b))

def task_4_113(f1=5.4,f2=19.255,f3=4.23,f4=0.28):

    def ifm5(f):
        if f > 5: return f
        else:     return 0

    s = ifm5(f1) + ifm5(f2) + ifm5(f3) + ifm5(f4)
    print('Сумма чисел, больших 5:',s)

def task_5_32(n):
    s = 0
    i = 1
    while i <= n:
        s+= 1/i
        i+= 1
    print(s)

def task_9_1():
    for i in range(3):
        print('8 8 8')

    for i in range(1,8):
        st = '{} '.format(i) * 5
        print(st)

    for i in range(10,90,10):
        st = (str(i) + ' ') * 4
        print(st)

    for i in range(12,92,10):
        st = (str(i) + ' ') * 4
        print(st)

    for i in range(5):
        for j in range(2,21):
            print(j,'',end='')
        print()

    for i in range(4):
        for j in range(15,2,-1):
            print(j,'',end='')
        print()

    j = 0
    for i in range(8):
        for k in range(8,j,-1):
            print(k,'',end='')
        j+= 1
        print()

    j = 2
    for i in range(8):
        for k in range(j,11):
            print(k,'',end='')
        j+= 1
        print()

    j = 3
    for i in range(9):
        for k in range(2,j):
            print(k,'',end='')
        j+=1
        print()

    j = 3
    for i in range(4):
        print((str(j)+' ') * j)
        j+= 1

    j = 21
    for i in range(5):
        print((str(j)+' ') * (j - 20))
        j+= 1

    j = 8
    for i in range(1,6):
        print(j * (str(i) + ' '))
        j-= 1

    for i in range(10,60,10):
        print((str(i) + ' ') * math.trunc(i/10))

    j = 5
    for i in range(5,10):
        print((str(i) + ' ') * j)
        j-= 1

    j = 5
    for i in range(5,30,5):
        print((str(i) + ' ') * j)
        j-= 1

    hun = 101
    for i in range(7):
        for j in range(6):
            print((str(hun+j) + ' '),end='')
        print()
        hun+= 10

    dec = 51
    for i in range(4):
        for j in range(8):
            print((str(dec + j) + ' '),end='')
        print()
        dec-= 10


def task_14_39(s1='анна',s2='трудный день',s3='олесе весело'):

    def ifpal(s):
        r = s[::-1]
        print(r,s)
        return r == s

    lspal = ''
    if ifpal(s1): lspal += s1 + ' '
    if ifpal(s2): lspal += s2 + ' '
    if ifpal(s3): lspal += s3 + ' '
    print('Палиндромы среди строк:',lspal)
