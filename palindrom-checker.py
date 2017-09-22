from deque import Deque

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

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

