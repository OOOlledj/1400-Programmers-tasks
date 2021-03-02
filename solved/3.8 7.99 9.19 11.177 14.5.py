import math
import random

#MATH.trunc

def task_3_8(N):
    if N <= 1642 or N >= 1942:
        return 'enormous N'
    N-= 1643
    row = math.trunc(N/15)+1
    return 'ряд № ' + str(row) + ' для ' + str(N+1)

def task_7_99():
    arr = []
    for i in range(10):
        arr.append(random.randint(1,50))
    arr.append(9999)
    print(arr)
    
    
    for i in range(1,len(arr)):
        if arr[i]%2==0 and arr[i-1]%2==0:
            return 'exist pair: №'+str(i)+' and №'+str(i+1)
    return 'does not exist'

def task_9_19():
    for i in range(120, 141):
        numdel = 0
        for j in range(1, i+1):
            if i%j==0:
                numdel+= 1
                #print(j)
        print(str(i) + ' has ' + str(numdel) + ' deviders')
    
def task_11_177():
    '''turns
    #a b c d e f
    to
    #b c d a e f
    (place 1st element on position k, and moves
    all element 2-k moves left on 1 pos)
    '''
    arr = ['a','b','c','d','e','f']
    k = 3                           #index to change (d -> a)
    resArr = []                     
    resArr.extend(arr[1:k+1])       #b c d
    resArr.extend(arr[0])           #b c d a
    resArr.extend(arr[k+1:len(arr)])#b c d a e f
                                    #a b c d e f
    return (resArr)
    
def task_14_5():
    def FullStart():
        return '*' * 60
    def BordStart():
        return '*' + ' ' * 58 + '*'
    for i in range(20):
        if i == 0 or i == 19:
            print(FullStart())
        else:
            print(BordStart())
    
    
    
'''
for i in range(1643,1643+68):
    print(task_3_8(i))


print(task_7_99())'''

'''task_9_19()'''

'''print(task_11_177()'''

'''task_14_5()'''