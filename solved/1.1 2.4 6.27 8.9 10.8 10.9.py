import math
import random

def task_1_1():
    print(31, 18, 79)
    
def task_2_4(a):
    return a*4    
    
def task_6_27():
    flag = 0
    toCheck = 100
    while (flag < 15):
        if toCheck % 19 == 0:
            print(flag+1,' ', toCheck)
            flag+= 1
        toCheck+= 1
        
def task_8_9(a):
    n = 2
    while True:
        if (1 + 1/n) >= a:
            n+= 1
        else:
            print(n)
            break
    return n
    
def task_10_8():
    return random.choice([0,1])

def task_10_9(laps = 100):
    # 1 - OREL
    # 0 - RESHKA
    print('\nfor ',laps,' "throws":\n')
    orel = 0
    resh = 0
    
    for i in range(laps):
        if task_10_8() == 1:
            orel+= 1
        else:
            resh+= 1
    print('OREL: ',orel/laps, orel)
    print('RESHKA: ',resh/laps, resh)
    
    

'''task_1_1()'''

'''print(task_2_4(4))'''

'''task_6_27()'''

'''task_8_9(1.1117)'''

'''task_10_9(laps=100)
task_10_9(laps=1000)'''