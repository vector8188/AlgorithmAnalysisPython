def anagramSolution5(s1, s2):
    # check if they are equal in length
    if len(s1) != len(s2):
        return False
    c1 = {}
    c2 = {}
    for w1 in s1:
        if not c1.get(w1):
            c1[w1] = 0
        else:
            c1[w1] = c1[w1] +1
    for w2 in s2:
        if not c2.get(w2):
            c2[w2] = 0
        else:
            c2[w2] = c2[w2] +1
    for k,v in c1.items():
        if c1.get(k) != c2.get(k):
            return False
    
    return True

print(anagramSolution5('earth', 'heart'))

