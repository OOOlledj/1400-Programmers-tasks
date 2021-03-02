import random
import math
def task_3_45(k):
    
    def isodd(k):
        #true=odd
        return k%2==0
    pair = 0
    for seq in range(10,99):
        pair+=2
        if (k==pair) or (k+1==pair):
            print(math.trunc(pair/2)) #1
            print(seq)                #2
            if isodd(k):                  #3
                print (seq%10)
            else:
                print(int(seq/10))
            

def task_4_102(a,b,c,d):
    arr = [a,b,c,d]
    arrmx = a
    arrmn = a
    for i in arr:
        if arrmx < i:
            arrmx = i
        if arrmn > i:
            arrmn = i
    print('min:',arrmn,'\nmax:',arrmx)
    

def task_10_19():
    nominal = ['шестерка', 'семерка', 'восьмерка', 
               'девятка', 'десятка', 'Валет', 
               'Дама', 'Король', 'Туз', ]
    print('выбрана ' + random.choice(nominal)        )
    return 'выбрана ' + random.choice(nominal)        

def task_12_65(sent):
    wrds = 0
    wflag = False
    for i in range(len(sent)):
        if sent[i]==' ':
            wflag=False
        else:
            if not wflag:
                wflag=True
                wrds+= 1
    print('sentance contain ',wrds,' words!')

def task_13_56(defin):
    chem = {
        'H':'Hydrogen',
        'Li':'Lithium',
        'Na':'Natrium',
        'Ca':'Calcium'
        }   
    if chem.get(defin) == None:
        print('does not exist!')
    else:
        print('Exists!')
