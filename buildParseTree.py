from binaryTree import BinaryTree
from stack import Stack
import operator

class buildParseTree():

	def __init__(self,fplist):
		self.fplist = fplist.split()


	def parseTree(self):
		# create an empty stack
		self.pStack = Stack()
		# create an empty Tree,
		self.eTree = BinaryTree('')
		# push an empty Tree up the stack.
		self.pStack.push(self.eTree)
		# start at very top of tree, and as name suggests, currentTree
		# tracks what is your current postition in the stack.
		self.currentTree = self.eTree
		for i in self.fplist:
			if i == '(':
				# Read ( as the first token. By rule 1,
				# create a new node as the left child of the root.
				# Make the current node this new child.
				self.currentTree.insertLeft('')
				# pushing up the stack to remember when required to pop.
				# which is in when we encounter a number, and according to
				# algorithm, we have to set current value to
				self.pStack.push(self.currentTree)
				self.currentTree = self.currentTree.getLeftChild()
			elif i not in ['+', '-', '*', '/', ')']:
				self.currentTree.setRootVal(int(i))
				parent = self.pStack.pop()
				self.currentTree = parent
			elif i in ['+', '-', '*', '/']:
				self.currentTree.setRootVal(i)
				self.currentTree.insertRight('')
				self.pStack.push(self.currentTree)
				self.currentTree = self.currentTree.getRightChild()
			elif i == ')':
				self.currentTree = self.pStack.pop()
			else:
				raise ValueError
		return self.eTree

	@classmethod
	def evaluate(cls,pt):
		opers = {'+':operator.add, '-':operator.sub,
		'*':operator.mul, '/':operator.truediv}
		leftC = pt.getLeftChild()
		rightC = pt.getRightChild()
		if leftC and rightC:
			f = opers[pt.getRootVal()]
			return f(cls.evaluate(leftC),cls.evaluate(rightC))
		else:
			return pt.getRootVal()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(buildParseTree.evaluate(pt.parseTree()))



print(pt.parseTree().getRootVal())
print(pt.parseTree().getRightChild().getRootVal())
print(pt.parseTree().getLeftChild().getRootVal())
print(pt.parseTree().getLeftChild().getLeftChild().getRootVal())
print(pt.parseTree().getLeftChild().getRightChild().getRootVal())
