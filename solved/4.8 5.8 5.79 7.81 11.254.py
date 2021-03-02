import math
import random


def task_4_8(x):
    if math.sin(x * math.pi / 180) >= 0:
        k = x ** 2
    else:
        k = abs(x)

    if x < k:
        f = abs(x)
    else:
        f = k * x

    print(f)


def task_5_8():
    blanc = " " * 5
    print("Фунты", blanc, "Кг")
    for i in range(1, 10):
        print(i, blanc + "   ", round(i * 0.453, 3))


def task_5_79():
    for num in range(1000, 9999):
        if num % 133 == 125 and num % 134 == 111:
            print(num)


def task_7_81(arr=None):
    if arr == None:
        arr = []
        for i in range(20):
            arr.append(random.randint(0, 99))

    def splitter(n):
        if n < 10:
            return [0, n]
        else:
            return [int(n / 10), n % 10]

    sumWin = 0  # b
    sumLose = 0  # v
    sumDraw = 0  # g
    sumDiff = 0  # d
    allCount = 0  # e

    for raw in arr:  # a
        mt = splitter(raw)
        if mt[0] < mt[1]:
            print('lose')
            sumLose += 1
        elif mt[0] > mt[1]:
            print('win')
            sumWin += 1
        else:
            print('draw')
            sumDraw += 1

        if abs(mt[0] - mt[1]) >= 3:
            sumDiff += 1

    allCount = sumWin * 3 + sumDraw + sumLose * 0
    print(arr)
    print(sumWin, sumLose, sumDraw, sumDiff, allCount)


def task_11_254(stk):
    nw = []
    neg = []
    pos = []
    for el in stk:
        if el >= 0:
            pos.append(el)
        else:
            neg.append(el)
    nw = neg + pos
    print(nw)

# task_4_8(-90)
# task_5_8()
# task_5_79()
# task_7_81([78, 91, 17, 56, 1, 32, 67, 36, 86, 17, 30, 93, 81, 59, 8, 92, 79, 10, 72, 19])
# task_11_254([4,5,-3,8,-10,-1,4,-2])
