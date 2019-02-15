class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data):

        if data == self.data:
            return True
        else:
            if data < self.data:
                if self.left is None:
                    return False
                else:
                    return self.left.search(data)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.search(data)

    def printTree(self):

        if self.left is not None:
            self.left.printTree()
        print(self.data)
        if self.right is not None:
            self.right.printTree()