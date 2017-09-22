from node import Node

class OrderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == []

	def search (self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

	def add(self, item):
		current = self.head
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				# inch worming again beacuse we want to insert the value between current value and next value.
				previous = current
				current = current.getNext()

    	temp = Node(item)
    	if previous == None:
    		# this is again to handle, first case.
        	temp.setNext(self.head)
        	self.head = temp
    	else:
        	temp.setNext(current)
        	previous.setNext(temp)
