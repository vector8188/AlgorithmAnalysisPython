class BinHeap:
    """Class for implementing BinHeap."""
    def __init__(self):
        """Bin heap constructor."""
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """Checks if the newly entered item is greater/lesser than parent."""
        while i > 0:
            if self.heapList[i] < self.heapList[i//2]:
                # if the i//2'th element(parent) is > i(children) then swap.
                # which means if the parent > chilren, we need to maintain
                # valid heap datastructure where parent are always less than
                # chilren.
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        print("i --> {}".format(i))
        result = i*2 <= self.currentSize
        print("Testing {} <= {} --> {}".format(i*2, self.currentSize, result))
        while i*2 <= self.currentSize:
            print("heaplist before swap is {}".format(self.heapList))
            mc = self.minChild(i)
            print("mc <-- {}".format(mc))
            print(
                "self.heapList[{}] is compared with self.heapList[{}]".format(
                    i, mc))
            if self.heapList[i] > self.heapList[mc]:
                print(
                    "self.heapList[{}]-->({}) > self.heapList[{}] --> ({})".
                    format(i, self.heapList[i], mc,  self.heapList[mc]))
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
                print("heaplist after swap is {}".format(self.heapList))
            print("i <-- mc".format(mc))
            i = mc
            result = i*2 <= self.currentSize
            print("i --> {} \n".format(i))
            print("Testing {} <= {} --> {}".format(
                i*2, self.currentSize, result))

    def minChild(self, i):
        print("Evaluating minimum of two leaf nodes")
        if i*2+1 > self.currentSize:
            print("i*2+1-->({}) > self.currentSize-->({})".format(
                i*2+1, self.currentSize))
            return i*2
        else:
            print(
                "self.heapList[{}] is compared with self.heapList[{}]".format(
                    i*2+1, i*2))
            if self.heapList[i*2+1] > self.heapList[i*2]:
                print(
                    "self.heapList[{}] --> {} is > self.heapList[{}] --> {}".
                    format(
                        i*2+1, self.heapList[i*2+1], i*2, self.heapList[i*2]))
                print(
                    "returning {} as an index of child with lesser value".
                    format(i*2))
                return i*2
            else:
                print(
                    "self.heapList[{}] --> {} is > self.heapList[{}] --> {}".
                    format(
                        i*2, self.heapList[i*2], i*2+1, self.heapList[i*2+1]))
                print(
                    "returning {} as an index of child with lesser value".
                    format(i*2+1))
                return i*2+1

    def delMin(self):
        print("hepList before deletion: {}".format(self.heapList))
        # select lowest element in the heap, which is root.
        retval = self.heapList[1]
        # select the last item in the list and move it in the front
        # in place of root, retval already have same value.
        self.heapList[1] = self.heapList[self.currentSize]
        # reduce the size of currentSize by one.
        self.currentSize = self.currentSize - 1
        # pop the highest item in the list
        self.heapList.pop()
        # percolate down the fatty, sink motherfucker sink.
        self.percDown(1)
        print("hepList after deletion: {}".format(self.heapList))
        return retval

    def buildHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
bh.delMin()
