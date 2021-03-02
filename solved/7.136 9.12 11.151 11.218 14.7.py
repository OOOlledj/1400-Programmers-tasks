import math
import random


def task_7_136():
    results = []
    for i in range(5):
        raw = random.randint(14, 25)
        results.append(raw)
        print('next result: ' + str(raw))
        print('best time: ' + str(min(results)) + '\n')
    return results
        
def task_9_12(enum = []): 
    
    classes = ['a','b','c','d']
    
    def classFiller():
        parralel = range(1,12) 
        enum = []
        for c in classes:
            for p in parralel:
                enum.append([c, p, random.randint(15, 28)])
        return enum
    
    if enum == []:
        enum = classFiller()
    #subtask (a)
    lessStudents = enum[0][2]
    lessStudentsCall = enum[0][0] + str(enum[0][1])
    
    for cl in enum:
        if cl[2] < lessStudents:
            lessStudents = cl[2]
            lessStudentsCall = cl[0] + str(cl[1])
    print('less students class: ' + lessStudentsCall + ', ' + str(lessStudents) + ' students')
    
    #subtask (b)
    parrSums = []
    for i in range(11):
        parrSums.append(0)
    for cl in enum:
        parrSums[cl[1]-1]+= cl[2]
    
    minParrSt = min(parrSums)
    minParrStIndex = parrSums.index(minParrSt)
    print(parrSums)
    print('less students in parralel: ' + str(minParrStIndex + 1) + ', ' + str(minParrSt))    
    
    clSums = []
    for i in range(4):
        clSums.append(0)
    for cl in enum:
        if cl[0]=='a' : pos=1
        if cl[0]=='b' : pos=2
        if cl[0]=='c' : pos=3
        if cl[0]=='d' : pos=4
        clSums[pos-1]+= cl[2]
        
    minClSt = min(clSums)
    minClStIndex = clSums.index(minClSt)
    print(clSums)
    if minClStIndex==0 : pos='a'
    if minClStIndex==1 : pos='b'
    if minClStIndex==2 : pos='c'
    if minClStIndex==3 : pos='d'
    print('less students in class row: ' + pos + ', ' + str(minClSt))  
    
    return enum
  
def task_11_151(arr = []):
    '''каждое сл. задание выполняется над предыдущим массивом,
    то есть arr меняется, так как arrOut = arr не создает новый
    экземпляр, а создает ссылку!!! В целом все выполняется верно'''
    if arr==[]:
        for i in range(10):
            arr.append(random.randint(10,100))
    print(arr)        
    
    #subtask(a)
    el5 = arr[4]
    el2 = arr[1]
    arrOut = arr
    arrOut[4] = el2
    arrOut[1] = el5
    print(arrOut)
    del arrOut
    
    #subtask(b)
    m, n = 4,7
    elm = arr[m-1]
    eln = arr[n-1]
    arrOut = arr
    arrOut[m-1] = eln
    arrOut[n-1] = elm
    print(arrOut)
    del arrOut
    
    #subtask(c)
    el3 = arr[2]
    elmax = max(arr)
    elmaxIndex = arr.index(elmax)
    arrOut = arr
    arrOut[2] = arr[elmaxIndex]
    arrOut[elmaxIndex] = el3
    print(arrOut)
    del arrOut
    
    #subtask(d)
    el1 = arr[0]
    elmin = min(arr)
    elminIndex = arr.index(elmin)
    arrOut = arr
    arrOut[0] = arr[elminIndex]
    arrOut[elminIndex] = el1
    print(arrOut)
    del arrOut
    
    return arr
    
def task_11_218(arr = []):
    
    if arr==[]:
        for i in range(15):
            arr.append(random.randint(10,100))
    print(arr)

    arrDiff = []
    for elem in arr:
        if elem not in arrDiff:
            arrDiff.append(elem)
    elements = len(arrDiff)
    print('Different array elements: ' + str(elements))
    return elements

def task_14_7():
    a,b,c,d=1,2,3,4
    def swap(x,y):
        x+= y
        y = x - y
        x-= y  
        return x,y
    a,b = swap(a,b)
    c,d = swap(c,d)
    print('{a b c d}',a,b,c,d)

'''print(task_7_136())'''

'''enum = task_9_12()'''

'''arr = task_11_151()'''

''''task_11_218()'''

task_14_7()
