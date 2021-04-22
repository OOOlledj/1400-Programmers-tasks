import math
import random

def task_3_9(n=7450):
    h = int(n/60/60)
    m = int((n/60)%60)
    s = n%60
    print('n секунд с начала отсчета это %i:%i:%i полных часов, минут, секунд' %(h,m,s))


def task_5_39():
    x = 2
    s = 1
    sign = -1
    for i in range(1,11):
        s+= sign * x**i * ((i+1)/(i+2))
        sign*= -1
        #print(i, x**i,((i+1)/(i+2)))
    print(s)

def task_7_29():
    marks = []
    for i in range(25):
        marks.append(random.randint(2,5))
    avr = 0
    for m in marks:
        avr+= m
    avr/= len(marks)
    print('Средняя оценка по математике: %f' %avr)

def task_12_182(s = 'I am in the kitchen, our kid play on garden, i kept all sugar'):
    words = s.split(' ')
    kstart = []
    for word in words:
        if word[0].lower() == 'k':
            kstart.append(word)
    print('Слово, начинающееся на "к" в предложении:',random.choice(kstart))

def task_13_19():
    weather = []
    for i in range(30):
        precipitation = random.randint(0,40)
        temperature = random.randint(-5,12)
        weather.append([precipitation,temperature])
    snow = 0
    rain = 0
    for day in weather:
        if day[1] > 0:
            rain+= day[0]
        else:
            snow+= day[0]
    print('За месяц выпало %i мм осадков в виде снега и %i в виде дождя' %(snow,rain))
