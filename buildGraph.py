from graphs import Graph


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wfile, 'r')
    # create buckets of word differ by one letter.
    for line in wfile:
        word = line.rstrip()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edge for words in the same bucket.
    for bkt in d.keys():
        for word1 in d.get(bkt):
            for word2 in d.get(bkt):
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g
