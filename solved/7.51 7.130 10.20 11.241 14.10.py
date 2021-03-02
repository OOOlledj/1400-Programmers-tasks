import random
import math

def task_7_51():
    
    sums = 0
    arr = [1,3,7,19,53,42,44,77]
    i = 0
    
    while i<8 and arr[i]%2 == 1:
        sums+= arr[i]
        i+= 1
    
    return sums

def task_7_130():
    repeater = 0
    flag = 0
    arr = [1,2,3,4,5, 12, 94, 1006, 2, 501, 722, 2, 45, 79, 504, 900, 2, 2, 111, 98]
    for i in range(len(arr)):
        repeater = arr[i]
        for j in range(i, len(arr)): 
            if i!=j and repeater == arr[j]:
                flag+=1
        if flag!=0:
            break
    return (repeater, flag)

def task_10_20():
    
    nominal = ['шестерка', 'семерка', 'восьмерка', 
               'девятка', 'десятка', 'Валет', 
               'Дама', 'Король', 'Туз', ]
    crop = ['пик', 'крест', 'червей', 'бубен']


    card =  'выбрана ' + random.choice(nominal) + ' ' + random.choice(crop)

    return card

def task_11_241():
    arrTme = [71, 44, 45, 80, 44, 107, 45, 78, 38, 57, 24, 103, 65, 120, 100, 99, 25, 82, 37, 78, 113, 111, 21, 26, 94]
    arrDst = [137, 94, 62, 216, 48, 204, 224, 44, 146, 150, 126, 128, 236, 177, 175, 148, 38, 134, 192, 174, 50, 186, 234, 94, 88]
    arrSpd = []
    
    minAvr = 0
    
    for i in range(25):
        if i==0:
            minAvr = arrDst[i] / arrTme[i]
            arrSpd.append(minAvr)#using 3 arrays
        else:
            nxtAvr = arrDst[i] / arrTme[i]
            arrSpd.append(nxtAvr)#using 3 arrays
            if nxtAvr < minAvr:
                minAvr = nxtAvr
    
    #compare results
    if minAvr == min(arrSpd):
        return str(minAvr*60) + ' km/h'
    else:
        return "error"

def task_14_10(a=None, b=None, c=None):
    if a == None: a = random.randint(1, 100)
    if b == None: b = random.randint(1, 100)
    if c == None: c = random.randint(1, 100)
    print(a,b,c)
    
    def calcs(var):
        return (math.sqrt(var)+var)/2
    
    return calcs(a) + calcs(b) + calcs(c)

'''print(task_7_51())

print(task_7_130())
        
print(task_10_20())

print(task_11_241())

print(task_14_10())'''