import math
import random

def task_2_3(a,x):
    a = math.sqrt((2*a+math.sin(abs(3*a)))/3.56)
    try:
        x = (3.2 + math.sqrt(1+x))/(abs(5*x))
    except (ZeroDivisionError):
        x = 'inf'
    print('f1(a)={}, f2(x)={}'.format(a,x))

def task_8_16(m=0.7):
    '''0.5 < m < 1'''
    i = 1
    while i < 10:
        step = i/(i+1)
        if step < m:
            print(step)
        i+= 1

def task_12_193(s1='123 456 199', s2='123 459 999 918 456 456'):
    s1 = s1.split(' ')
    s2 = s2.split(' ')
    print(s1,s2)
    alr = []
    out = 'Слово "{}"{}входит в предложение'
    for w in s1:
        flag = ' не '
        isin = False
        for cmp in s2:
            if cmp == w:
                isin = True
                alr.append(w)
                flag = ' '
        print(out.format(w,flag))

def task_13_18(s):
    art = []
    for i in range(28):
        fname = random.randint(1,500)
        sname = random.randint(1,500)
        school = random.randint(1,10)
        cls = random.randint(4,11)
        art.append({
            'fname':fname,
            'sname':sname,
            'school':school,
            'cls':cls})
    sc1011 = []
    for st in art:
        if st.get('school') == s and st.get('cls') in (10,11):
            sc1011.append(st)
    print('Ученики школы %i старших классов:\n' %s, sc1011)

def task_14_2(sym='$',n=10):
    print(sym*n)
