from node import Node

"""

append(item) adds a new item to the end of the list making it the last item in the collection. 
             It needs the item and returns nothing. Assume the item is not already in the list.
index(item) returns the position of item in the list. It needs the item and returns the index. 
             Assume the item is in the list.
insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. 
             Assume the item is not already in the list and there are enough existing items to have position pos.
pop() removes and returns the last item in the list. It needs nothing and returns an item. 
             Assume the list has at least one item.
pop(pos) removes and returns the item at position pos. It needs the position and returns the item.
              Assume the item is in the list.


"""

class UnorderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		counter = 0
		while current != None:
			counter = counter + 1
			current = current.getNext()
		return counter

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found :
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
			if previous == None:
				# this handles case when we found the 'item' during first attempt, which led to 'found' --> True
				# and previous remained 'None' as that was the 'item' was first item in the unordered list.
				self.head = current.getNext()
			else:
				previous.setNext( current.getNext())

	def append(self,item):
		current = self.head
		previous = None
		while current != None:
			previous = current
			current = current.getNext()
		previous.setNext(Node(item))

	def index(self, item):
		current = self.head
		found = False
		counter = 0
		while current != None and not found :
			if current.getData() == item:
				found = True
			else:
				counter = counter + 1
				current = current.getNext()
		return counter

	def insert(self, item, index):
		current = self.head
		index_counter = 0 
		previous = None
		temp = Node(item)
		while index_counter < index:
			index_counter = index_counter + 1
			previous = current
			current = current.getNext()
			if index_counter == index:
				temp = Node(item)
				temp.setNext(current)
				previous.setNext(temp)

	def pop(self, index=0):
		current = self.head
		index_counter = 0 
		previous = None
		while index_counter < index:
			index_counter = index_counter + 1
			previous = current
			current = current.getNext()
			if index_counter == index:
				previous.setNext(current.getNext())


