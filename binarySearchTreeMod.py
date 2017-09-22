class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree(TreeNode):
    def __init__(self):
        # self.root is refrence to TreeNode, which is root
        # of primary TreeNode
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        # checks if there is root
        # if there is a root, lets transverse along tree
        if self.root:
            self._put(key, val, self.root)
        else:
            # else if there is not root, lets set a root
            # which is a TreeNode instance
            self.root = BinarySearchTree()
            self.root.key = key
            self.root.value = val
        self.size = self.size + 1

    def _put(self, key, val, currentNode):

        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:

                #currentNode.leftChild = BinarySearchTree(
                #    key, val, parent=currentNode)
                currentNode.leftChild = BinarySearchTree()
                currentNode.leftChild.key = key
                currentNode.leftChild.val = val
                currentNode.leftChild.parent = currentNode
                import pdb;pdb.set_trace()
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                #currentNode.rightChild = BinarySearchTree(
                #    key, val, parent=currentNode)
                currentNode.rightChild = BinarySearchTree()
                currentNode.rightChild.key = key
                currentNode.rightChild.val = val
                currentNode.rightChild.parent = currentNode
                import pdb;pdb.set_trace()

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        if key == currentNode.key:
            return currentNode
        if key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        # this method allows to access instance[index]
        # format.
        return self.get(key)

    def __contains__(self, key):
        """
        __contains__ overloads the 'in' operator
        allows us to do something simliar to
        if 'Northfield' in myZipTree:
            print("oom ya ya")
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key was not found')
        elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size = self.size - 1
        else:
            raise KeyError('Error, key was not found')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            # current Leaf has only one child
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:
            # The node to be deleted has only one child.
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    # this is a root node, replace it's data with it's
                    # left children
                    self.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.value,
                        currentNode.leftChild,
                        currentNode.rightChild
                    )
            else:
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    # this is a root node, replace it's data with it's
                    # left children
                    self.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.value,
                        currentNode.leftChild,
                        currentNode.rightChild
                    )

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.hasLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return self

    def findMin(self):
        if self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent



mytree = BinarySearchTree()
mytree[17] = "17"
mytree[5] = "5"
mytree[35] = "35"
mytree[2] = "2"
mytree[11] = "11"
mytree[9] = "9"
mytree[16] = "16"
mytree[7] = "7"
mytree[29] = "29"
mytree[38] = "38"

del(mytree[5])
print(mytree[5])
print(mytree[7])
print(mytree.size)
