import math
import random

def task_2_23(a,b):
    p = 2*a + 2*b
    d = math.sqrt(a**2 + b**2)
    print('Периметр: %i, диагональ: %i' %(p,d))

def task_4_58(a,b,c):
    pair = False
    if a == b:
        pair = True
    if a == c:
        pair = True
    if b == c:
        pair = True
    print("Наличие хотя бы одной равной пары чисел: %s" %pair)

def task_10_11():
    return random.randint(1,6)

def task_11_155(arr):
    larr = len(arr)

    fneg = None
    i = 0
    while i < larr:
        if arr[i] < 0:
            fneg = i
            break
        i+= 1
    lpos = None
    i = larr - 1
    while i > 0:
        if arr[i] > 0:
            lpos = i
            break
        i-= 1
    print(arr)
    if lpos != None and fneg != None:
        arr[lpos], arr[fneg] = arr[fneg], arr[lpos]
    print(arr)

def task_13_16():
    cdate = input('current date (DD:MM:YYYY):')
    students = [[1,1,'11:02:1998'],[2,2,'22:10:1998'],[3,3,'03:04:2000'],
            [5,4,'15:03:1999'],[5,5,'03:12:1998'],[6,6,'17:07:1998'],
            [7,7,'29:11:1997'],[8,8,'26:05:2000'],[9,9,'30:01:1999']]
    for prs in students:
        if prs[2][0:5] == cdate[0:5]:
            print('Сегодня день рождения у ',prs[0],prs[1])
