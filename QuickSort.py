def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if last > first:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint -1)
        quickSortHelper(alist, splitpoint +1, last)

def partition(alist, first, last):
    pivotValue = alist[first]
    leftmark = first+1
    rightmark = last
    print("pivotValue:{}\nleftmark:{}\nrightmark:{}\n".format(pivotValue, leftmark, rightmark))

    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark = leftmark +1
            print("increasing leftmark by 1,  leftmark:{}".format(leftmark))
        while rightmark >= leftmark and pivotValue  <= alist[rightmark]:
            rightmark = rightmark - 1
            print("decreasing rightmark by 1, rightmark:{}".format(rightmark))
        if leftmark > rightmark:
            print("INFLECTION:leftmark:{} > rightmark:{}".format(leftmark, rightmark))
            done = True
        else:
            print("alist before exchange:{}".format(alist))
            print("arranging in asc order: exchanging {}, with {}".format(alist[leftmark], alist[rightmark]))
            swap = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = swap
            print("alist after exchange:{}".format(alist))

    print(
        "{} > {}; we need to put lesser value in front of the list".format(
            pivotValue, alist[rightmark])
        )
    swap = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = swap
    print(alist)

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
#print(alist)

