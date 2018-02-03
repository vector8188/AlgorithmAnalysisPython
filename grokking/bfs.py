# Python builtin import
from collections import deque
# custom Deque import.
from deque import Deque as Dq

def findword(vertex,item_to_be_searched):
    return vertex == item_to_be_searched
    


def bfs(graph, start,item_to_be_searched):
    search_que = Dq()
    searched = []
    path = []

    search_que.addFront(graph[start])

    path.append(start)
    while search_que.size() > 0:
        current_item = search_que.removeFront()
        for current_vertex in current_item:
            if not current_vertex in searched:
                if findword(current_vertex, item_to_be_searched):
                    print ("True")
                    return True
                else:
                    search_que.addFront(graph[current_vertex])
                    searched.append(current_vertex)
    print ("False")
    return False

class Vertex:
    """
    Adjacency List implementation of a graph vertex
    We create a very simple class to represent or Graph nodes so we can use it in our Graph Traversal Algorithms
    Just the bare essentials were included here
    """
    def __init__(self, vert_id):
        """
        Constructor
        :param vert_id: The id that uniquely identifies the vertex.
        """
        self.vert_id = vert_id          # simple type
        self.neighbors = []             # type List[Vertex]
        self.status = 'undiscovered'    # undiscovered | discovered | explored

        self.distance = -1              # shortest distance from source node in shortest path search
        self.previous = None            # previous vertex in shortest path search

    def addVertex(self, vertex):
        """
        Adds a new vertex as an adjacent neighbor of this vertex
        :param vertex: new Vertex() to add to self.neighbors
        """
        self.neighbors.append(vertex)

    def getNeighbors(self):
        """
        Returns a list of all neighboring vertices
        :return: list of vertexes
        """
        return self.neighbors


def shortestPathBFS(vertex):
    """
    Shortest Path - Breadth First Search
    :param vertex: the starting graph node
    :return: does not return, changes in place
    """
    if vertex is None:
        return

    queue = deque()                                  # our queue is a list with insert(0) as enqueue() and pop() as dequeue()
    queue.append(vertex)

    while len(queue) > 0:
        current_vertex = queue.popleft()                    # remove the next node in the queue
        next_distance = current_vertex.distance + 1     # the hypothetical distance of the neighboring node

        for neighbor in current_vertex.getNeighbors():

            if neighbor.distance == -1 or neighbor.distance > next_distance:    # try to minimize node distance
                neighbor.distance = next_distance       # distance is changed only if its shorter than the current
                neighbor.previous = current_vertex      # keep a record of previous vertexes so we can traverse our path
                queue.append(neighbor)


def traverseShortestPath(target):
    """
    Traverses backward from target vertex to source vertex, storing all encountered vertex id's
    :param target: Vertex() Our target node
    :return: A list of all vertexes in the shortest path
    """
    vertexes_in_path = []

    while target.previous:
        vertexes_in_path.append(target.vert_id)
        target = target.previous

    return vertexes_in_path


# Build a graph to use in our example shortest path search
# This is done roughly just for the example here to get the structure illustrated.
# In practice, you will probably be given a pre made graph or build it more elegantly programmatically
vert_1 = Vertex(1)
vert_2 = Vertex(2)
vert_3 = Vertex(3)
vert_4 = Vertex(4)
vert_5 = Vertex(5)
vert_6 = Vertex(6)
vert_7 = Vertex(7)
vert_8 = Vertex(8)
vert_9 = Vertex(9)
vert_10 = Vertex(10)

vert_1.addVertex(vert_2)
vert_2.addVertex(vert_3)
vert_3.addVertex(vert_4)
vert_3.addVertex(vert_5)
vert_5.addVertex(vert_6)
vert_6.addVertex(vert_7)
vert_1.addVertex(vert_8)
vert_8.addVertex(vert_9)
vert_8.addVertex(vert_10)
vert_10.addVertex(vert_7)


# Lets set out source and target vertexes and find the shortest path between them
source = vert_1
target = vert_7

# Find the shortest path from our source vertex to every other vertex.
# The path data should be saved by reference in each vertex and available to us afterwards
shortestPathBFS(source)

# Trace the shortest path back from the target vertex to the source vertex
vertexes_in_path = traverseShortestPath(target)

# Display the results
print('shortest path length: ', len(vertexes_in_path))
print('shortest path: ', vertexes_in_path[::-1])     # print our shortest path in reverse order - from source to target

"""
the output for the sample graph should be:
shortest path length:  3
shortest path:  [8, 10, 7]
"""


if __name__ == "__main__":
    graph = {}
    graph["fool"] = ["pool", "foil", "foul", "cool"] 
    graph["pool"] = ["poll"] 
    graph["foil"] = ["fail"]
    graph["foul"] = []
    graph["cool"] = []
    graph["fail"] = []
    graph["poll"] = ["pole", "pall"]
    graph["pall"] = []
    graph["pole"] = ["pope", "pale"]
    graph["pope"] = []
    graph["pale"] = ["page", "sale"]
    graph["page"] = ["sage"]
    graph["sale"] = []

    bfs(graph,"fool","sage")
    
    


