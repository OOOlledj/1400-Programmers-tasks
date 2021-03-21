import math
import random

def task_1_11(name):
    print('{} - это чемпион'.format(name))

def task_2_5(r):
    return 2*r

def task_2_37(F):
    return F * 1.8 + 32

def task_8_3(a):
    i = 1
    while True:
        seq = 1/i
        if seq >= a:
            print(seq)
        else:
            break
        i+= 1

def task_8_5(a):
    i = 2
    while True:
        seq = 1 + 1/i
        if seq >= a:
            print(seq)
        else:
            break
        i+= 1
