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
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

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

