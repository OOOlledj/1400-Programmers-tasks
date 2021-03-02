import math
import random


def task_3_14(n):
    pod = math.trunc((n-1)/54) + 1
    etj = (math.trunc((n-1)/6) + 1) % 9
    cnt = math.trunc(n-1)%6 + 1
    print('Квартира находится на %i этаже %i подъезда, %iя по порядку' % (etj,pod,cnt))

def task_3_49(hAng):
    '''Угол часовой стрелки в градусах'''
    allMinutes = hAng * 2
    hh = math.trunc(allMinutes/60)
    mm = math.trunc(allMinutes) % 60
    mAng = mm*6
    print('Полное время: %i:%i' % (hh,mm))
    print('Угол минутной стрелки составляет', mAng, 'градусов')
    
def task_9_53():
    '''Поиск числа Рамануджана—Харди'''
    buff = []
    comm = []
    for i in range(1, 100):
        for j in range(1, 100):
            if j not in buff:
                comm.append([[i, j], i ** 3 + j ** 3])
        buff.append(i)
    #Обнуляем буффер и анализируем полученные последовательности
    del buff
    buff = []
    foundFlag = False
    for i in comm:
        for j in comm:
            if j not in buff and i != j:
                if i[1] == j[1]:
                    print(i,j)      #Искомый результат выведется единожды,
                    foundFlag = True#и цикл прервется с помощью флага и break
                    break
        if foundFlag:
            break
        buff.append(i)
    del buff
    del comm

def task_10_3():
    a = int(input())
    b = int(input())
    a,b = min(a,b), max(a,b)
    n = random.randint(1, 20)
    m = random.randint(1,20)
    print('m=%i, n=%i' % (m,n))
    arrn = []
    for i in range(n):
        arrn.append(random.randint(a,b))
    arrm = []
    for i in range(m):
        arrm.append(random.random() * n)
    print(arrn)
    print(arrm)

def task_12_63(w2,wx,st):
    count = 0
    for i in range(len(st)-1):
        if st[i]+st[i+1]=='po':
            count+=1
    print('Буквосочетание "po" входит', count, 'раз')
    
    count = 0
    for i in range(len(st)-1):
        if st[i]+st[i+1]==w2:
            count+=1
    print('Буквосочетание из двух букв "%s" входит', count, 'раз')
    
    count = 0
    def extractor(wx,st,i):
        comp = ''
        for j in range(i,len(wx)+i):
            comp+= st[j]
        return comp
    for i in range(len(st) - len(wx) + 1):
        if extractor(wx,st,i) == wx:
            count+=1
    print('Некоторое буквосочетание "%s" входит', count, 'раз')

task_10_3()