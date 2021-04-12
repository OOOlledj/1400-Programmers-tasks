import math
import random

def task_4_3(x):
    if x > 0:
        y = math.sin(x**2)
    else:
        y = 1+ 2 * math.sin(x)**2
    print('y(x) = %f' %y)

def task_7_84(seq = [1,2,3,4,5,-1,8]):
    pos = 0
    for elem in seq:
        if elem > 0:
            pos+= 1
    if pos > 5:
        word = ' '
    else:
        word = (' не ')
    print('Количество положительных чисел{}превышает 5'.format(word))

def task_11_88(arr = [1,8,19, 45, 16, 22],lim = 15):
    sover = 0
    cnt = 0
    for elem in arr:
        if elem < lim:
            sover+= elem
            cnt+= 1
    print('Среднее арифметическое чисел, меньших {}: {}'.format(lim,sover/cnt))

def task_12_111(word = 'somethings'):
    nw = ''
    i = 0
    if len(word)%2 == 0:
        while i < len(word):
            nw+= word[i+1]+word[i]
            i+= 2
        print(nw)

def task_14_37(
        s1='what does the fox says',
        s2='Synthwave brings me back to times when nothing mattered',
        char='o'):

    def symrole(s,char):
        countchar = 0
        for elem in s:
            if elem == char:
                countchar+= 1
        return round(countchar*100/len(s), 3)


    print('% of char "{}" in s1:'.format(char), symrole(s1, char),'%')
    print('% of char "{}" in s2:'.format(char), symrole(s2, char),'%')

