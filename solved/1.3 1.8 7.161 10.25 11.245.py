import random

def task_1_3():
    print('%i\n%i' %(50,10))

def task_1_8():
    value = int(input())
    print('Вы ввели число: %i' %(value))

def task_7_161():
    teamCount = []
    n = 20
    for i in range(n):
        teamCount.append(random.randint(1,25))
   #min = [team N, points]
    min = [0,teamCount[0]]
    for i in range(n):
        if min[1] > teamCount[i]:
            min = [i, teamCount[i]]
    print('Наименьшее число очков (%i) набрала команда №%i' %(min[1],min[0]))

def task_10_25():
    def a():
        a = random.randint(1,8)
        b = random.randint(1,8)
        c = a
        d = b + 1
        print([a,b,c,d])

        if a == 1:
            c = a + 1
        elif a == 8:
            c = a - 1
        else:
            c = random.choice([a+1,a-1])
        print([a, b, c, d])

    def b():
        a = random.randint(1, 8)
        b = random.randint(2, 8)
        c = a
        d = b - 1
        print([a, b, c, d])

        if a == 1:
            c = a + 1
        elif a == 8:
            c = a - 1
        else:
            c = random.choice([a + 1, a - 1])
        print([a, b, c, d])

    def v():
        a = random.randint(1, 8)
        b = random.randint(2, 8)
        while True:
            c = random.choice([a+1,a-1,a+2,a-2])
            d = random.choice([b+1,b-1,b+2,b-2])
            if (c>=1 and d>=1) and (c<=8 and d<=8):
                if (abs(a-c) + abs(b-d) == 3):
                    print([a,b,c,d])
                    break
    #final call
    a()
    b()
    v()

def task_11_245():
    n = 10
    a, b = [], []
    for i in range(n):
        a.append(random.randint(-10,10))
    for i in range(n):
        if (i+1)%2 == 0:
            b.append(a[i]**2)
        else:
            b.append(2*a[i])
    print(a)
    print(b)

