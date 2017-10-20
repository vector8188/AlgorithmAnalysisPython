from graphs import Graph

"""
find a sequence of moves that allow the knight to visit every square on the board exactly once. 
"""

def knightGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = posToNodeId(row, col, bdsize)
            newPositions = genLegalMoves(row, col, bdsize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdsize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, column, board_size):
    return (row*board_size) + column

def genLegalMoves(x, y, bdsize):
    newMoves = []
    moveOffsets = [
        (-1,-2),(-1,2),(-2,-1),(-2,1),
        ( 1,-2),( 1,2),( 2,-1),( 2,1)
        ]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdsize):
    if x >= 0 and x < bdsize:
        return True
    return False

    