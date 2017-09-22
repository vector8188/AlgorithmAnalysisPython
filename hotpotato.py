from queue import Queue

def hotPotato(namelist, num):
    namequeue = Queue()

    for name in namelist:
        namequeue.enqueue(name)
    # keep doing the following when only one child is left in the queue
    while namequeue.size()>1:
        for i in range(num):
            # Assume that the child holding the potato will be at the front of the queue. 
            # Upon passing the potato, the simulation will simply dequeue and then 
            # immediately enqueue that child, putting her at the end of the line.
            # So Basically creating a circle.
            namequeue.enqueue(namequeue.dequeue())
        # remove front child from the queue.
        namequeue.dequeue()
    # only one child with hot potato is left in the Queue, Deque that as well. 
    return namequeue.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))