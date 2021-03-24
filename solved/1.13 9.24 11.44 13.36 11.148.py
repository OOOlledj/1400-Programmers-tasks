import math
import random

def task_1_13(n):
    print('Следущее: %i, предыдущее: %i' %(n+1,n-1))

def task_9_24(a, b):

    def countdivs(n):
        count = 0
        for i in range(1,n):
            if n % i == 0:
                count+= 1
        return count

    topdiv = 2
    abdivs = []
    for n in range(a,b):
        cd = countdivs(n)
        abdivs.append([n, cd])
        topdiv = cd if cd > topdiv else topdiv

    tops = []
    for elem in abdivs:
        if elem[1] == topdiv:
            tops.append(elem)

    if len(tops) > 1:
        minelem = tops[0]
        for elem in tops:
            if minelem[0] > elem[0]:
                minelem = elem
        print('Меньшее из чисел с кол-вом делителей {}'.format(minelem[0]))
        maxelem = tops[0]
        for elem in tops:
            if minelem[0] < elem[0]:
                maxelem = elem
        print('Большее из чисел с кол-вом делителей {}'.format(maxelem[0]))
    else:
        print("Число с наибольшим количеством делителей:", tops[0][0])

def task_11_44():
    jan = []
    for i in range(31):
        jan.append(random.randint(0,400))
    summ = 0
    for i in jan:
        sum+= i
    print('В январе выпало %i мм осадков' %summ)

def task_11_148():
    n = random.randint(5,15)
    arra = []
    for i in range(n):
        arra.append(random.randint(0,25))
    print('Изначальный массив:', arra)
    for i in range(n-1):
        if arra[i] > arra[i+1]:
            arra[i+1],arra[i] = arra[i], arra[i+1]
    print('Модифицированный массив:', arra)

def task_13_36():

    def sorth(stud):
        i = 0
        while i < 25:
            minh = min(stud[i:25])
            stud.remove(minh)
            stud.insert(i,minh)
            i+= 1
        return stud

    stud = []
    i = 0
    while i < 25:
        geth = random.randint(160,194)
        if geth not in stud:
            stud.append(geth)
            i+= 1
        else:
            pass
    stud = sorth(stud)
    print('Самый высокий и низкий ученики:', stud[24],stud[0])
    print('2-3 по высоте ученики:', stud[22],stud[23])
    print('Двое самых высоких учеников:',stud[23],stud[24])


task_13_36()

