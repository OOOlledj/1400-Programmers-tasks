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
    pythonFile = ''
    for i in toDo:
        pythonFile += i
        if i==toDo[len(toDo)-1]:
            pythonFile += '.py'
        else:
            pythonFile += ' '
    with open('solved/' + pythonFile, 'w'):
        print(pythonFile)


def TaskAccomp():
    
    file = open('Container.txt', 'r+')
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