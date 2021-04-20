import math
import random

def task_2_32(N,mon=5000,syst=16000,keyb=2800,ms=1500):
    print("Цена 3-х компьютеров:",3*(mon+syst+keyb+ms))
    print("Цена %i-х компьютеров:" %N, N * (mon + syst + keyb + ms))

def task_4_47(a=4.8,b=16.901,c=0.7815):
    print('Неравенство a<b<c:', (b>a) and (b<c))
    print('Неравенство b>a>c:', (a<b) and (a>c))

def task_5_55():
    s = 0
    i = 1
    sign = -1
    while i <= 10:
        s+= sign * (i**2)
        sign*= -1
        i+= 1
    print(s)

def task_6_46(n):

    arr = []
    while n >= 1:
        arr.append(n % 10)
        n = math.trunc(n / 10)
    arr.reverse()

    max1to5 = 0
    max5to1 = len(arr) - 1

    # max 1->5
    for i in range(len(arr)):
        if arr[i] > arr[max1to5]:
            max1to5 = i
    # max 5->1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[max5to1]:
            max5to1 = i
    min1to5 = 0
    min5to1 = len(arr) - 1

    # min1 1->5
    for i in range(len(arr)):
        if arr[i] < arr[min1to5]:
            min1to5 = i
    # min1 5->1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < arr[min5to1]:
            min5to1 = i
    print(max1to5,max1to5,min1to5,min5to1)
    '''Пример:
    12345, max = 5, min = 1, порядковые номера:
    01234, maxn= 4, minn= 0
    987162, max = 9, min = 1, порядковые номера:
    012345, maxn= 0, minn= 3
    и так далее
    '''
#task_6_46(12345)
#task_6_46(987162)
#task_6_46(567904)

def task_13_13(a,b):
    class events:

        def __init__(self,data,year,month,day):
            self.data = data
            self.year = year
            self.month = month
            self.day = day

    arr_events = []
    for i in range(20):
        data = 'event ' + str(i)
        year = random.randint(1930,2021)
        month = random.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
            day = 31
        if month in [4,6,9,11]:
            day = 30
        else:
            day = 28
        day = random.randint(1,day)

        event = events(data,year,month,day)
        arr_events.append(event)

    event1 = arr_events[a]
    event2 = arr_events[b]
    print(event1.data + ': %i.%i.%i' %(event1.day,event1.month,event1.year))
    print(event2.data + ': %i.%i.%i' %(event2.day,event2.month,event2.year))
    #pre, aft
    if event1.year > event2.year:
        pre = event2
        aft = event1
    elif event1.year < event2.year:
        pre = event1
        aft = event2
    else:
        if event1.month > event2.month:
            pre = event2
            aft = event1
        elif event1.year < event2.year:
            pre = event1
            aft = event2
        else:
            if event1.day > event2.day:
                pre = event2
                aft = event1
            elif event1.day < event2.day:
                pre = event1
                aft = event2
            else: print("Все случилось в один день")
    print(pre.data,'предшествовало',aft.data)



