import math
import random
from string import Template

def task_2_9(x,y):
    #task(a)
    za = 2*x**3 - 3.44*x*y + 2.3*x**2 - 7.1*y + 2
    print(za)
    #task(b)
    zb = 3.14*((x+y)**3) + 2.75*y**2 - 12.7*x - 4.1
    print(zb)

def task_3_30(n):
    print('hundrs: ' + str(n/100))
    print('decs: ' + str(n/10))
        
def task_6_40(a):
    count = 0
    stra = str(a)
    for i in range(len(stra)):
        if stra[0]==stra[i]:
            count+= 1
    print('in %(numb)d %(dig)s meets %(count)d times' % {'numb':a,'dig':stra[0],'count':count})
        
def task_7_18():
    dev = random.randint(1,25)
    digits = []
    for i in range(10):
        digits.append(random.randint(1,100))
    com = sum(digits)
    output = Template('sum %(com)d$flag devided by %(dev)d' % {'com':com,'dev':dev})
    if com%dev == 0:
        print(output.substitute(flag = ''))
    else:
        print(output.substitute(flag = ' is not'))

def task_7_52():
    arr = []
    for i in range(10):
        arr.append(random.randint(0,23))
    print(arr)
    #subtask(a)
    suMore20 = 0
    for i in arr:
        if i>20:
            suMore20+= i
    output = Template('sum of 20<x is$flag bigger than 100 (it is %(suMore20)d)' % {'suMore20':suMore20})
    if suMore20 > 100:
        print(output.substitute(flag = ''))
    else:
        print(output.substitute(flag = ' not'))
        
    #subtask(b)
    suLess50 = 0
    for i in arr:
        if i < 50:
            suLess50+= i
    output = Template('sum of 50>x is$flag devided by 2 (it is %(suLess50)d)' % {'suLess50':suLess50})
    if suLess50%2 == 0:
        print(output.substitute(flag = ''))
    else:
        print(output.substitute(flag = ' not'))
    
'''task_2_9(0,0)'''

'''task_3_30(1540)'''

'''task_6_40(1451)'''

#task_7_18()

#task_7_52()