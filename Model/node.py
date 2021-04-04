class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Get
    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    # Set
    def setData(self, data):
        self.data = data

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
