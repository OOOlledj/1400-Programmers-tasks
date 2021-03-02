import math
import random

def task_2_26(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(distance)
    
def task_5_75():
    for i in range(100,200):
        if i % 3 == 0:
            print(i)
            
def task_6_53(n,a,b,k):
    pwr = 10
    arr = []
    while n >= 1:
        arr.append(n % 10)
        n = int(n/10)
    print(arr)
    
    #subtask a
    aflag = False
    if a in arr:
        aflag = True
        
    #subtask b
    bflag = False
    if b in arr:
        bflag = True
            
    #subtask c
    count = 0
    for i in arr:
        if i == a:
            count+=1
    kflag = False
    if count > k:
        kflag = True
        
    #subtask d
    dflag = False
    if aflag and bflag:
        dflag = True
        
    #output:
    print('a is in stock: ',aflag)
    print('b is not in stock: ', not(bflag))
    print('a meets more than k times: ', kflag)
    print('a and b both met in stock: ', dflag)
    
def task_8_14(a):
    flag_found = False
    div = 1
    while flag_found == False:
        res = 1.0/div
        print(res)
        if res < a:
            flag_found = True
        else:
            div+= 1
    print(div, res)
            
def task_11_32(arr):
    print(arr)
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = abs(arr[i])
        if i==0 or i%2==0: # 1 mean 0, 2 mean 1 etc...
            arr[i] = math.sqrt(arr[i])
    print(arr)
            
'''task_2_26(0,4,0,8)
task_2_26(1,1,8,8)'''

#task_5_75()

#task_6_53(123445,8,5,2)

#task_8_14(0.0185)

#task_11_32([11.4,-12.2,-4.4444,-15.2,0.144,19.871,22.10,-1998.22,-56.91])