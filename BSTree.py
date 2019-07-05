class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def get(self):
        return self.key
    def set(self, key):
        self.key = key
    def getChildren(self):
        children = []
        if(self.left != None):
            children.append(self.left)
        if(self.right != None):
            children.append(self.right)
        return children

class BST:
    def __init__(self):
        self.root = None
    def setRoot(self, key):
        self.root = Node(key)
    def insert(self, key):
        if(self.root is None):
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)
    def insertNode(self, currentNode, key):
        if(key <= currentNode.key):
            if(currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if(currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)
    def find(self, key):
        return self.findNode(self.root, key)
    def findNode(self, currentNode, key):
        if(currentNode is None):
            return False
        elif(key == currentNode.key):
            return True
        elif(key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)
    def inorder(self):
        def _inorder(v):
            if(v is None):
                return
            if(v.left is not None):
                _inorder(v.left)
            print(v.key)
            if(v.right is not None):
                _inorder(v.right)
        _inorder(self.root)
