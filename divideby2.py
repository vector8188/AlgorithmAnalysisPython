from stack import Stack

def divideBy2(decNumber):
    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber=decNumber//2
    
    binnumber=""
    while not s.isEmpty():
        binnumber=binnumber+str(s.pop())
    
    return binnumber

def baseconverter(decNumber,base):
    stringlist="0123456789ABCDEF"
    s = Stack()

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber=decNumber// base
    
    basenumber=""
    while not s.isEmpty():
        basenumber=basenumber+stringlist[s.pop()]
    
    return basenumber

print(baseconverter(26,26))
print(baseconverter(256,16))
print(baseconverter(25,8))