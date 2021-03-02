import math
import random

def task_9_20(k):
    for i in range(1,k+1):
        s=0
        print(i,end='')
        for j in range(1,i+1):
            if i%j==0:
                print('+',end='')
        print()

def task_9_27():
    s=0
    for i in range(50,71):
       for j in range(1,i+1):
           if i%j==0:
               s+= j
    print(s)

def task_11_2():
    arr = []
    for i in range(10):
        arr.append(int(input()))
    print(arr)
    
def task_11_27():
    n = random.randint(10,20)
    arr = []
    for q in range(n):
        arr.append(random.randint(1,100))
    print(arr)
    for i in range(0,n):
        if (i+1) % 2 == 0:
            print(arr[i],'',end='')
    print('| ', end='')
    for j in range(0,n):
        if (j+1) % 2 != 0:
            print(arr[j],'',end='')
            
def task_14_12():
    y = 0
    pair = [[2,5],[6,3],[1,4]]
    for i in pair:
        y+= (i[0] + math.sin(i[0])) / (math.sin(i[1]) + i[1])
    print(y)
    
    y=0
    pair = [[1,4],[7,5],[3,2]]
    for i in pair:
        y+= (i[0] + math.sin(i[1])) / (i[1] + math.sin(i[0]))
    print(y)
    
task_14_12()
