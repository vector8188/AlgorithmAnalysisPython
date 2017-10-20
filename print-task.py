import random

from queue import Queue


class Printer:
    # ppm is the number of pages processed by the printer per minute.
    def __init__(self, ppm):
        self.pagerate  = ppm
        self.currentTask = None
        self.timeRemaning = 0

    
    def tick(self):
        if self.timeRemaning != None:
            self.timeRemaning = self.timeRemaning - 1
            if self.timeRemaning <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        return False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaning = newtask.getPages()* 60/self.pagerate


class Task:
     # pages is the number of pages requested by the student per print task.
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.getStamp()
    
def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if ( not labprinter.busy() and not printQueue.isEmpty() ):
            nexttask = printQueue.dequeue()
            # print(currentSecond)
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # print(currentSecond)
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))



def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5)
     
