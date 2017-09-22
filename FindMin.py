import time
from random import randrange

def findMin(alist):
    overallMin = alist[0]
    for i in alist:
        isSmallest = True
        for j in alist:
            if i > j:
                isSmallest = False
            if isSmallest:
                overallMin = i
    return overallMin

def findMin2(alist):
    minsofar = alist[0]
    for i in alist:
        if minsofar > i:
            minsofar = i
    return minsofar


for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    starttime = time.time()
    print(findMin(alist))
    endtime =  time.time()
    print("size: %d, time: %f"% (listSize, endtime-starttime))

for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    starttime = time.time()
    print(findMin2(alist))
    endtime =  time.time()
    print("size: %d, time: %f"% (listSize, endtime-starttime))