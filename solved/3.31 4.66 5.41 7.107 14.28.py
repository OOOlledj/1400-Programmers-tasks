import math
import random

def task_3_31(n):
    thds = math.trunc(n/1000)
    hnds = math.trunc(n/100)
    '''
    or current hundreds
    hnds = math.trunc((n%1000)/100)
    '''
    print('hundreds: {} ,thousands: {}'.format(hnds,thds))

def task_4_66(a1,a2,a3,b1,b2,b3):
    A = sorted((a1, a2, a3))
    B = sorted((b1, b2, b3))
    if (
        (A[0] >= B[0] and A[1] >= B[1] and A[2] >= B[2]) or
        (A[0] >= B[1] and A[1] >= B[2] and A[2] >= B[0]) or
        (A[0] >= B[2] and A[1] >= B[0] and A[2] >= B[1])
        ):
        print('Коробку можно поместить в чемодан')
    else:
        print('коробка в чемодан не поместится')

def task_5_41(x,n):
    power = 1
    summ = 0
    i = 1
    while ((x!=0) and (i <= n)):
        #first is for case, when len(x)>n
        #second is counting n numbers from the end
        power*= x % 10
        summ+= x % 10
        x = math.trunc(x / 10)
        i+= 1
    print('p={},s={}'.format(power, summ))

def task_7_107(x):
    a = []
    n = random.randint(15,35)
    for i in range(12):
        a.append(random.randint(1,50))
    i = 0
    print('Среднее арифметическое')
    while i < 12:
        if a[i] > n:
            print('х и a%i : %f' %(i,(x+a[i])/2))
        i+= 1

class task_14_28:

    def __init__(self, dig6):
        self.dig = dig6

    def __calc3dig(self, dxyz):
        return (dxyz%10 +
                math.trunc(dxyz/10)%10 +
                math.trunc(dxyz/100)%10)

    def iflucky(self):
        s123 = self.__calc3dig(self.dig % 1000)             #123
        s456 = self.__calc3dig(math.trunc(self.dig / 1000)) #456
        if s123 == s456:
            print('Число "счастливое"')
        else:
            print('Число не является "счастливым"')

    def sum3(self, dxyz):
        return self.__calc3dig(dxyz)
'''
obj = task_14_28(123456)
obj.iflucky()
print(obj.sum3(123))
print(obj.sum3(255))
'''