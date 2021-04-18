import random
import math

def task_4_111(a=1,b=2,c=3,d=4):
    s = 0
    if a % 2 == 0: s+= 1
    if b % 2 == 0: s+= 1
    if c % 2 == 0: s+= 1
    if d % 2 == 0: s+= 1
    print('Количество четных чисел:',s)

def task_5_20():
    for i in range(1,10):
        fl = round(i/10,2)
        print("%.4f" %(math.sqrt(fl)))

def task_6_61(n = 12345):

    def makecopy(arr):
        narr = []
        for a in arr:
            narr.append(a)
        return narr

    arr = []
    while n >= 1:
        arr.append(n % 10)
        n = math.trunc(n / 10)
    arr.reverse()
    #print(arr)
    #[1,2,3,4,5]

    max115 = 0
    max215 = 0
    maxarr = makecopy(arr)
    #max1 1->5
    for i in range(len(maxarr)):
        if maxarr[i] > maxarr[max115]:
            max115 = i
    maxarr[max115] = 0
    #max2 1->5
    for i in range(len(maxarr)):
        if maxarr[i] > maxarr[max215]:
            max215 = i
    print('max 1,2 in 1->5:',max115+1,max215+1)

    max115 = 0
    max215 = 0
    maxarr = makecopy(arr)
    #max1 5->1
    for i in range(len(maxarr)-1,-1,-1):
        if maxarr[i] > maxarr[max115]:
            max115 = i
    maxarr[max115] = 0
    #max2 5->
    for i in range(len(maxarr)-1,-1,-1):
        if maxarr[i] > maxarr[max215]:
            max215 = i
    print('max 1,2 in 5->1:',max115+1,max215+1)


    min115 = 0
    min215 = 0
    minarr = makecopy(arr)
    # min1 1->5
    for i in range(len(minarr)):
        if minarr[i] < minarr[min115]:
            min115 = i
    minarr[min115] = 9
    # min2 1->5
    for i in range(len(minarr)):
        if minarr[i] < minarr[min215]:
            min215 = i
    print('min 1,2 in 1->5:',min115 + 1, min215 + 1)

    min115 = 0
    min215 = 0
    minarr = makecopy(arr)
    # max1 5->1
    for i in range(len(minarr) - 1, -1, -1):
        if minarr[i] < minarr[min115]:
            min115 = i
    minarr[min115] = 9
    # max2 5->
    for i in range(len(minarr) - 1, -1, -1):
        if minarr[i] < minarr[min215]:
            min215 = i
    print('min 1,2 in 5->1:',min115 + 1, min215 + 1)

def task_11_4():
    arr = []
    for i in range(20):
        arr.append('#')
    print(arr)
    print(len(arr))

def task_13_44(s,ns = ['IAMNEW', 5, 5, 5, 4, 4, 4, 5, 5, 5, 2]):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    arr = []
    for i in range(25):
        name = ''
        for j in range(6):
            name+= random.choice(alf)
        marks = []
        for j in range(10):
            marks.append(random.randint(2,5))
        arr+= [[name] + marks]
    #print(arr)
    arr.insert(s-1,ns)
    print('Годовые оценки учеников по 10 предметам')
    print('с учетом нового ученика, %i-го по списку' %s)
    for student in arr:
        print(student)



task_13_44(4)