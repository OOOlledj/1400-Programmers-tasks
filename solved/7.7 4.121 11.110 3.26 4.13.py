import random

def task_3_26(xyz):
    
    '''START SUB'''
    def subtask_3_26(arr):
        size = len(arr)
        result = []
        
        for i in range(size):
            result.append(
                str(arr[i % size]) + 
                str(arr[(i+1) % size]) + 
                str(arr[(i+2) % size]))
            
        return result
    '''END OF SUB'''
    
    if xyz > 999 or xyz < 100:
        return 'Must be three-digit'
    
    x = int(xyz/100)
    y = int(xyz/10%10)
    z = xyz%10
    
    if x==y or y==z or x==z:
        return 'Digits mus be different'
    
    arr = [x,y,z]
    
    result = subtask_3_26(arr)
    del arr
    arr = [x,z,y]
    result+= subtask_3_26(arr)
    
    return print(result)

def task_4_13(m1,v1,m2,v2):
    '''item 1 and item 2, use the same valuations: kg and m^3 or else'''
    if m1/v1 > m2/v2:
        return '1st material denser'
    else:
        return '2nd material denser'

def task_4_121(x,y):
    if x < 1:
        return 'zone I'
    elif x > 1 and x < 5:
        return 'zone II'
    elif x > 5:
        return 'zone III'

def task_7_7():
    #work on input:
    arrRes = list(map(int, input().split(' ')))
    
    #1/R = 1/R1 + 1/R2 ... + 1/Rn => dev (Devider)
    #R = 1/Devider
    
    dev = 0
    for r in arrRes:
        dev+= 1/r
    R = 1/dev
    return R    


def task_11_110():
    arr30 = []
    for i in range(30):
        arr30.append(random.randint(1,100))

    
    noRepArr = []
    for i  in range(30):
        if arr30[i] not in noRepArr:
            noRepArr.append(arr30[i])
    
    print(arr30)
    return (30-len(noRepArr))

'''task_3_26(123)

print(
     task_4_13(1,1, 2.5,0.03175))

print(
     task_4_121(-3, 4))


print(
      task_7_7())

print(
      task_11_110())

'''