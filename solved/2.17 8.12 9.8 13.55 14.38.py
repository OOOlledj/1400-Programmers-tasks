import math
import random

def task_2_17(a,b,h):
    return a + b + 2 * math.sqrt(h**2 + ((a-b)/2)**2)

def task_8_12(a):
    for n in range(2,18):
        counter = 1
        for j in range (2,n):
            counter+= 1/j
        if counter > a:
            print('n is:',n-1,',float:',counter)

def task_9_8():
    students = []
    for i in range(14):
        students.append([
            random.randint(2,5),
            random.randint(2,5),
            random.randint(2,5)])

    def prstud(st):
        for i in st:
            print(i)

    non2 = 0
    for stud in students:
        if 2 not in stud:
            non2+= 1
    print('Студентов, сдавших сессию без двоек:',non2)

    i=0
    comm = 0
    while i < 3:
        mark45 = 0
        mark2 = 0
        j=0
        while j < 14:
            if students[j][i] == 5 or students[j][i] == 4:
                mark45+= 1
            if students[j][i] == 2:
                mark2+= 1
            j+=1
        if mark45 == 14:
            comm+= 1
        print('Количество двоек по предмету %i:' %(i+1),mark2)
        i+= 1
    print('Количество предметов, по которым получено только 4 или 5:',comm)
    #prstud(students)

def task_13_55():
    chem = {
        'H': 'Hydrogen',
        'Li': 'Lithium',
        'Na': 'Natrium',
        'Ca': 'Calcium'
    }
    name = input()
    if name in chem:
        print('Такой элемент в спииске есть')

def task_14_38(s1='Я куплю тебе йод',s2='йодированная сетка'):
    i1 = 0
    i2 = 0
    i = 0
    while i < len(s1):
        if s1[i] == 'й':
            i1 = i
        i+= 1
    i = 0
    while i < len(s2):
        if s2[i] == 'й':
            i2 = i
        i+= 1
    if i2 > i1: i = 2
    elif i1 > i2: i = 1
    else: i = 0
    print('Больший индекс буквы "й" в предложении:',i)