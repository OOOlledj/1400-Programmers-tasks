import random
import math

def task_1_5():
    print(1,'\n'+str(2))
    
def task_3_20(a):
    # a is xyz
    #task (a)
    z = a%10
    print('z: ',z)
    #task (b)
    y = int(a/10)
    print('decs: ',y)
    #task (c)
    y = y%10
    x = int(a/100)
    s = x+y+z
    print('sum: ',s)
    #task (d)
    comp = x*y*z
    print('composition: ',comp)
    #print(a,x,y,z)

def task_10_5():
    arr = []
    for i in range(30):
        arr.append(random.randint(0,5))
        if arr[i] % 2 != 0:
            print(arr[i])
    return arr

def task_11_20():
    
    def generatePair():
        return [random.randint(2,9),
                random.randint(2,9)]
    
    arr = []
    #a,b = 0
    for i in range(20):
        while True:
            a,b = generatePair()
            if ([a,b] or [b,a]) not in arr:
                break
        arr.append([a,b])
        print('composition of ',a,' and ',b,': ')
        answer = int(input())
        if answer == a*b:
            print(True)
        else:
            print(False)

def task_11_222():
    main = 1
    for i in range(2,101):
        main*= i
    print(main)
    arr = []
    main = str(main)
    for i in range(len(main)):
        arr.append(int(main[i]))
        print(arr[i])

#task_1_5()
#task_3_20(459)
#arr = task_10_5()
#task_11_20()
#task_11_222()