from queue import Queue
from graphs import Graph, Vertex


def bfs(g, start):
    # start is the starting vertex of the graph,
    # as it's the starting point, set distance to zero 
    # also predecessor to 'None' as this was the starting
    # point.
    start.setDistance(0)
    start.setPred(None)
    # initialize an empty Queue to hold the vertices.
    # enuqeue `start` in the Queue
    vertQueue = Queue()
    vertQueue.enqueue(start)
    # check if vertices Queue has any Queue items to be explored.
    # if there are any items that need to be explored we have 
    # not searched far enough.
    while (vertQueue.size() > 0):
        # take out `dequeue` the first Item in the vertices Queue.
        # and assign it to  `currentVert`.
        # for loop now goes over all the connections for this vertex
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            # nbr is the current node in question,
            # if it was marked white, which means that it was 
            # never discovered and as a flag mark it was `grey`
            if (nbr.getColor == 'white'):
                nbr.setColor('grey')
                # set distance for nbr vertex to be +1 from `currentVertex`
                nbr.setDistance(currentVert.getDistance()+1)
                # now set nbr predecessor to be current vertex
                # and then we need to put `nbr` in  vertQueue as 
                # nbr needs to be explored as well for nodes. 
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        # when we reach here it means that currentVert connections have been completley explored.
        # and set the color to black as a marker.
        currentVert.setColor('black')
