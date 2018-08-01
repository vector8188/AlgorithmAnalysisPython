from deque import Deque
"""
def palchecker(inputStr):
	stillEqual = True
	inputDeque = Deque()
	for letters in inputStr:
		inputDeque.addFront(letters)
	while inputDeque.size() > 1:
		front = inputDeque.removeFront()
		back = inputDeque.removeRear()
		if front != back:
			stillEqual = False
	return stillEqual
"""
def palCheckerlist(inputStr):
    stillTrue = True
    inputDeque = []
    for letter in inputStr:
        inputDeque.append(letter)
    print(inputDeque)
    while len(inputDeque) > 0:
        front  = inputDeque.pop(0)
        if len(inputDeque)>0:
            back = inputDeque.pop(-1)
            if front != back:
                stillTrue = False
    return stillTrue

print(palCheckerlist("lsdkjfskf"))
print(palCheckerlist("radar"))


