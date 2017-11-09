from graphs import Graph, Vertex

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
            self.dfsvisit(aVertex)
    
    def dfsvisit(self, startVertex):
        print("vertex {}: color {}".format(startVertex, startVertex.getColor()))
        print("setting color gray")
        startVertex.setColor('gray')
        print("vertex {}: color {}".format(startVertex, startVertex.getColor()))
        self.time += 1
        startVertex.setDiscovery(self.time)
        print("setting discovery time {} for vertex, {}".format(startVertex.getDiscovery(),startVertex ))
        for nextVertex in startVertex.getConnections():
            print("connections for vertex {} are {}. ".format(startVertex, startVertex.getConnections()))
            print("     LOOP: vertex {}: color {}".format(nextVertex, nextVertex.getColor()))
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                print("RECURSION: making recursive call on vertex {}".format(nextVertex))
                self.dfsvisit(nextVertex)
        print("setting color black")
        startVertex.setColor('black')
        print("vertex {}: color {}".format(startVertex, startVertex.getColor()))
        self.time += 1
        startVertex.setFinish(self.time)
        print("setting finish time {} for vertex, {}".format(startVertex.getFinish(), startVertex ))

if __name__ == '__main__':

    g = DFSGraph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')

    a = g.getVertex('a')
    b = g.getVertex('b')
    c = g.getVertex('c')
    d = g.getVertex('d')
    e = g.getVertex('e')
    f = g.getVertex('f')

    g.addEdge(a,b)
    g.addEdge(a,d)
    g.addEdge(b,c)
    g.addEdge(b,d)
    g.addEdge(d,e)
    g.addEdge(e,b)
    g.addEdge(e,f)
    g.addEdge(f,c)
    g.dfs()

