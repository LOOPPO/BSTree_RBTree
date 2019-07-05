class NodeRB:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = "Red"
    def get(self):
        return self.key
    def set(self, key):
        self.key = key
    def setColor(self, color):
        self.color = color
    def getChildren(self):
        children = []
        if(self.left != None):
            children.append(self.left)
        if(self.right != None):
            children.append(self.right)
        return children
    def getColor(self):
        return self.color

class RBT:
    def __init__(self):
        self.nil = NodeRB(None)
        self.nil.setColor("Black")
        self.root = self.nil
    def setRoot(self, key):
        self.root = NodeRB(key)
        self.root.setColor("Black")
        self.root.p = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if(y.left != self.nil):
            y.left.p = x
        y.p = x.p
        if(x.p == self.nil):
            self.root = y
        elif(x == x.p.left):
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if(y.right != self.nil):
            y.right.p = x
        y.p = x.p
        if(x.p == self.nil):
            self.root = y
        elif(x == x.p.left):
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y
    def insert(self, key):
        if(self.root is self.nil):
            self.setRoot(key)
        else:
            self.insertNode(NodeRB(key))
    def insertNode(self, z):
        y = self.nil
        currentNode = self.root
        while (currentNode != self.nil):
            y = currentNode
            if(z.key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        z.p = y
        if(z.key < y.key):
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        return self.insertFixup(z)
    def insertFixup(self, z):
        while ( z.p.color == "Red"):
            if(z.p == z.p.p.left):
                y = z.p.p.right
                if(y.color == "Red"):
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color = "Red"
                    z = z.p.p
                else:
                    if (z == z.p.right):
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = "Black"
                    z.p.p.color = "Red"
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if (y.color == "Red"):
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color ="Red"
                    z = z.p.p
                else:
                    if (z == z.p.left):
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = "Black"
                    z.p.p.color = "Red"
                    self.leftRotate(z.p.p)
        self.root.color = "Black"
    def find(self, key):
        return self.findNode(self.root, key)
    def findNode(self, currentNode, key):
        if(currentNode is self.nil):
            return False
        elif(key == currentNode.key):
            return True
        elif(key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)
    def inorder(self):
        def _inorder(v):
            if(v is self.nil):
                return
            if(v.left is not self.nil):
                _inorder(v.left)
            print(str(v.key) + " " + v.color)
            if(v.right is not self.nil):
                _inorder(v.right)
        _inorder(self.root)
