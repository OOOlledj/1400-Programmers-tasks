import math
import random

def task_7_155(spawn = False, seq = [1,2,3,4,5,-3,6,7,8,9,10,11,12,0]):
    if spawn:
        seq = []
        for i in range(20):
            seq.append(random.randint(1,100))
    print(seq)
    clen = 1 #отслеживаемая длина
    mlen = 0 #наибольшая длина
    melm = seq[0] #отслеживаемый элемент - первый в массиве
    i = 1
    while i < len(seq)-1:
        if melm < seq[i]: #Если следующий больше предыдущего
            clen+= 1      #+1 к отслеживаемой длине
        else:             #Иначе сброс текущего счетчика
            clen = 0
        if clen > mlen:   #обновляем max длину, если она увеличилась
            mlen = clen
        melm = seq[i]
        i+= 1
    print('Длина наибольшей возрастающей последовательности: %i' %(mlen))

def task_10_27(n = 2000):
    #a
    #прямоугольник (ограничения): p>x>0, 1>y>0
    #половина синусоиды: y=sin(x)
    k = 0
    Sp = 1*math.pi
    for i in range(n):
        dot = [
            random.random() * math.pi,
            random.random()]
        if dot[1] <= math.sin(dot[0]):
            k+= 1
    square = Sp * k/n
    print('Площадь половины синусоиды: %f' %square)
    #б
    #Ограничение: x=3, y=x**2, y=0
    #Прямоугольник: x=3,y=9
    k = 0
    Sp = 3*9
    for i in range(n):
        dot = [
            random.random()*3,
            random.random()*9]
        if dot[1] <= dot[0]**2:
            k+= 1
    square = Sp * k/n
    print('Площадь фигуры, ограниченной x=3, y=0, y=x**2: %f' %square)


def task_11_18():

    def simple(n):
        c = 0
        for i in range(1,n):
            if n%i == 0:
                c+= 1
        return c == 1 or n == 1

    arra = []
    i = 300
    while len(arra) != 20:
        if i % 13==0 and i % 17==0:
            arra.append(i)
        i+= 1
    print(arra)
    arrb = []
    i = 1
    while len(arrb) != 30:
        if simple(i):
            arrb.append(i)
        i+= 1
    print(arrb)

def task_11_35(arr = [1.1,2.5,-3.7,0.4,28.1,-17.04,9.99,6.48,-1.25]):
    arra = []
    arrb = []
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            a = arr[i] + arr[1]
        else:
            a = arr[i] + arr[0]
        arra.append(a)
        if i%2 == 0:
            b = arr[i] + 1
        else:
            b = arr[i] * 2
        arrb.append(b)
        i+=1
    print(arra,'\n',arrb)

def task_12_172(a = 'ababvgdqq', b = 'abbadq'):
    '''try:
    ababvgd | abbad = T | T
    ababvgd | abbadq = F | F
    ababvgdqq | abbadq = T | F
    '''
    def presult(word,flag):
        if flag:
            word += 'можно'
        else:
            word += 'нельзя'
        return word

    sta = []
    stb = []
    for s in a:
        sta.append(s)
    for s in b:
        stb.append(s)
    #a
    flag = True
    for i in stb:
        if i not in sta:
            flag = False
            break
    print(presult('Второе слово из первого (по наличию букв вообще) составить ', flag))
    #b
    flag = True
    for i in stb:
        if stb.count(i) != sta.count(i):
            flag = False
            break
    print(presult('Второе слово из первого (по равному количеству букв) составить ',flag))

task_12_172()

