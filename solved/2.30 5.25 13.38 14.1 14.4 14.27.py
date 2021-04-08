import math
import random

def task_2_30(ax=-2,ay=4,bx=4,by=4,cx=4,cy=-3,dx=-1,dy=-1):
    def getlen(x1,x2,y1,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    def gets(A,B,C):
        p = (A+B+C)/2
        return math.sqrt(p*(p-A)*(p-B)*(p-C))
    ab = getlen(ax,bx,ay,by)
    bc = getlen(bx,cx,by,cy)
    ca = getlen(cx,ax,cy,ay)
    cd = getlen(dx,cx,dy,cy)
    da = getlen(dx,ax,dy,ay)
    sabc = gets(ab,bc,ca)
    scda = gets(cd,da,ca)
    #print(ab,bc,ca,cd,da)
    s = sabc + scda
    print('площадь выпуклого четырехугольника: %f' %s)

def task_5_25():
    i = 2.2
    while i < 4.4:
        print('%i,%i' %(math.trunc(i),math.trunc(i*10%10)))
        i+=0.2

def task_13_38():
    pers = []
    for i in range(16):
        sname = i
        age = random.randint(18,45)
        army = random.choice([True,False])
        pers.append([sname,age,army])
    #a
    youn = pers[0]
    for per in pers:
        if per[2] and youn[1] > per[1]:
        #если военнообязанный и возраст меньше чем у пред. по списку
            youn = per
    print('Самый молодой военнообязанный:',youn)
    #b
    armyt = []
    armyf = []
    for per in pers:
        if per[2]:
            armyt.append(per)
        else:
            armyf.append(per)

    def elder3(army):
        armye = []
        for i in range(3): #сделаем по 3 на список
            for j in range(len(army)): #ищем человека-точку отсчета
                if army[j] not in armye:
                    maxa = army[j]
                    break
            for per in army:
                if per[1] > maxa[1] and per not in armye:
                #проверяем возраст и присутствие в конечном списке
                    maxa = per
            if maxa not in armye:
            #добавление в список
                armye.append(maxa)
        return armye

    armyte = elder3(armyt)
    armyfe = elder3(armyf)
    print('Старшие военнообязанные:',armyte)
    print('Старшие невоеннообязанные:', armyfe)


def task_14_1():
    print(60*'*')

def task_14_4(method=1):
    def call1():
        for i in range(20):
            task_14_1()
    def call2():
        for i in range(20):
            for j in range(60):
                print('*',end='')
            print('\n',end='')

    if method == 1: call1()
    if method == 2: call2()



def task_14_27(a=1245,b=19899):

    def cnum(n):
        num = 0
        while True:
            if n < 1:
                break
            else:
                n/= 10
                num+= 1
                print(n)
        return num

    anum = cnum(a)
    bnum = cnum(b)
    word = 'Цифр больше в числе '
    if anum > bnum:
        word+= 'a (' + str(anum) +')'
    elif bnum > anum:
        word+= 'b (' + str(bnum) +')'
    else:
        word = 'Равное кол-во цифр в числах'
    print(word)
