class ABB:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    # ADD Root

    def add(self, node):
        if self.root is None:
            self.root = node

        else:
            self.addRoot(self.root, node)

    def addRoot(self, pivot, node):

        if pivot is None:
            return True

        if node.getData().getRoute() > pivot.getData().getRoute():
            if self.addRoot(pivot.getRight(), node):
                pivot.setRight(node)
                return False

        if node.getData().getRoute() < pivot.getData().getRoute():
            if self.addRoot(pivot.getLeft(), node):
                pivot.setLeft(node)
                return False
        return False


    def inOrder(self, pivot, list):
        if pivot is not None:
            self.inOrder(pivot.getLeft(), list)
            list.append([pivot.getData().getRoute(),pivot.getData().getMaterial(),pivot.getData().getAmount()])
            self.inOrder(pivot.getRight(), list)
            return list
        return list