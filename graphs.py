class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = "white"
        self.pred = None
        self.disc = 0
        self.fin = 0

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDistance(self, distance):
        self.distance = distance

    def setPred(self, pred):
        self.pred = pred

    def getDistance(self):
        return self.distance

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setDiscovery(self,dtime):
        self.disc = dtime

    def getDiscovery(self):
        return self.disc

    def setPred(self,p):
        self.pred = p
    
    def getPred(self):
        return self.pred
    
    def setFinish(self,ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        self.vertList[key] = Vertex(key)
        return Vertex(key)

    def getVertex(self, key):
        return self.vertList.get(key)

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, origin, destination, cost=0):
        if origin not in self.vertList:
            self.addVertex(origin)
        if destination not in self.vertList:
            self.addVertex(destination)
        self.vertList.get(origin).addNeighbor(self.vertList.get(destination), cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
