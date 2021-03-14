import math
import random

def task_3_46(k):
    ione = 0
    i101 = 101
    while i101 <= 150:
        if ione + 1 <= k and ione + 3 >= k:
            print('число %i' %i101)
            if k % 3 == 1:
                num = math.trunc(i101 / 100)
            elif k % 3 == 2:
                num = math.trunc(i101 / 10) % 10
            elif k % 3 == 0:
                num = i101 % 10
            print('k-я цифра это %i' %num)
        i101+= 1
        ione+= 3

def task_4_123(pts):
    if pts == 0:
        print('Проигрыш')
    elif pts == 1:
        print('Ничья')
    elif pts == 3:
        print('Победа')
    else:
        print('Некорректный ввод')

def task_9_13():
    school = []
    for i in range(11):
        school.append([])
        for j in range(4):
            school[i].append(random.randint(15,30))

    for i in range(11):
        mnpr = school[i][0]
        cls = 'А'
        for j in range(4):
            if mnpr > school[i][j]:
                mnpr = school[i][j]
                if j == 0: cls = 'А'
                elif j == 1: cls = 'Б'
                elif j == 2: cls = 'В'
                elif j == 3: cls = 'Г'
        print('Наимешьний класс в параллели %i это' %(i+1),cls,'|',mnpr)

    for i in range(4):
        mncl = school[0][i]
        prl = i
        for j in range(11):
            if mncl > school[j][i]:
                mncl = school[j][i]
                prl = j
        if i == 0: cls = 'А'
        elif i == 1: cls = 'Б'
        elif i == 2: cls = 'В'
        elif i == 3: cls = 'Г'
        print('Наименьший %s-класс в %i параллели' %(cls,prl+1),'|',mncl)

def task_9_52(q,p):

    def issimple(n,p):
        nod = 1
        for i in range(2,max(n,p)):
            if n%2 == 0 and p%2==0:
                nod = i
        if nod == 1:
            return True
        else:
            return False

    for i in range(1,q):
        if q % i == 0 and issimple(i,p):
            print(i)

def task_12_91(phr='Захожу в чащобу и чувствую, что сыро тут'):
    for i in range(len(phr)-1):
        cmpl = phr[i] + phr[i+1]
        if cmpl == 'чу' or cmpl == 'щу':
            print('Буквосочетание найдено! %i символ строки' %(i+1))

