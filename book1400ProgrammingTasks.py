'''
Generate 5 random tasks from one-name book
'''

import random

taskLim = {1:17, #tasks in each paragraph
           2:38,
           3:51,
           4:145,
           5:94,
           6:83,
           7:171,
           8:19,
           9:54,
           10:28,
           11:261,
           12:199,
           13:61,
           14:40}

def ChapTaskGen():
    chap = random.randint(1,14)
    task = '.' + str(random.randint(1,taskLim[chap]-1))
    return str(chap) + task
    
def TasksToDo(toDo):
    '''Print tasks to do'''
    for i in toDo:
        print(i)

def TaskAccomp():
    
    file = open('book1400Container.txt', 'r+')
    finished = file.read()
    finished = finished.split(' ')
    #print(finished)
    
    toDo = []
    for i in range(5):
        task = ChapTaskGen()
        while True:
            if task not in finished and task not in toDo:
                break
            else:
                task = ChapTaskGen()
        toDo.append(task)
        WRITETOFILE = toDo[i] + ' '
        file.write(WRITETOFILE)
        
    TasksToDo(toDo)

TaskAccomp()