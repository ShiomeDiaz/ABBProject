class Node:

    def __init__(self, dato, material, amount):
        self.dato = dato
        self.material = material
        self.amount = amount
        self.left = None
        self.right = None

    # Get
    def getDato(self):
        return self.dato

    def getMaterial(self):
        return self.material

    def getAmount(self):
        return self.amount

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    # Set
    def setDato(self, dato):
        self.dato = dato

    def setMaterial(self, material):
        self.material = material

    def setAmount(self, amount):
        self.amount = amount

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
