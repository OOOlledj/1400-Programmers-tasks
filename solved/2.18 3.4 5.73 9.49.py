import math
import random

def task_2_18(x,y):
    
    zNum = x+(2+y)/(x**2)
    zDiv = y+(1/(math.sqrt(x**2+10)))
    z = zNum/zDiv
    print(z)
    
    q = 7.25 * math.sin(x * math.pi/180) - abs(y)
    print(q)
    
def task_3_4(n,k):
    each = k // n
    corz = k % n
    print("Каждому достанется ", each," яблок")
    print("В корзинке будет ", corz," яблок")

def task_5_73():
    hyp = 45
    kat = 30
    while  kat >= 0:
        ang = math.acos(kat/hyp) * 180 / math.pi
        print(kat/10, " угол равен: ",ang)
        kat-= 2
        

def task_9_49(n):
    
    def simple(x):
        count = 0
        for i in range(1,x+1):
            if x % i == 0:
                count+= 1
        #print(x,count)
        if count == 2 or i==1:
            return True
        else:
            return False
    
    for i in range(1,n+1):
        if simple(i):
            if n % i == 0:
                print(i)


#task_2_18(10,15)
#task_3_4(27,914)
#task_5_73()
#task_9_49(212)