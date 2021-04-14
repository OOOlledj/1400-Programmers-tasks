import math
import random

def task_5_43(n=5):
    a = [1]
    for k in range(1, n+1):
        a.append(a[k-1]*k + 1/k)
    print(a)

def task_6_44(n):
    nums = str(n)
    maxn = int(nums[0])
    minn = int(nums[0])
    for num in nums:
        if maxn < int(num):
            maxn = int(num)
        if minn > int(num):
            minn = int(num)
    if (maxn-minn)%2 == 0:
        odd = ' '
    else:
        odd = ' not '
    print(maxn,'-',minn,'is{}odd'.format(odd))

def task_14_16(x1=1,y1=1,x2=3,y2=3,x3=4,y3=0):

    def xyline(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    A = xyline(x1,y1,x2,y2)
    B = xyline(x2,y2,x3,y3)
    C = xyline(x3,y3,x1,y1)

    P = A+B+C
    print('Периметр:',P)

def task_14_25():

    def fact(n):
        f = 1
        for i in range(2,n+1):
            f*= i
        return f

    print('Значение выражения:',(2*fact(5) + 3*fact(8)) / (fact(6) + fact(4)))

def task_14_36(c = 'a',
        s1='calculate factorial',
        s2='activities in it sphere',
        s3='insurance service is online'):

    def countchar(s,c):
        val = 0
        for sym in s:
            if sym == c:
                val+= 1
        return val

    symbols = countchar(s1,c)+countchar(s2,c)+countchar(s3,c)
    print('Общее количество символа "%s" в предложениях: %i' %(c,symbols))
