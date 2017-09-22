class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key

def buildTree():
	root = BinaryTree('a')
	root.insertLeft('b')
	root.insertRight('c')
	b_node = root.getLeftChild()
	b_node.insertRight('d')
	c_node = root.getRightChild()
	c_node.insertLeft('e')
	c_node.insertRight('f')


ttree = buildTree()