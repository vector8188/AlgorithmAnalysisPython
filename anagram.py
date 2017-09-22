def anagramSolution(s1,s2):
    c1 = {}
    for i in s1:
        if i in c1:
            c1[i] = c1[i] + 1
        else:
            c1[i] = 1

    for i in s2:
        anagram = True
        if i not in c1:
            anagram = False
            return anagram
    return anagram


print(anagramSolution('apple','pleap'))