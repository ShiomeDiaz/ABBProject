class Mine:
    def __init__(self, route, material, amount):
        self.route = route
        self.material = material
        self.amount = amount

    # Get
    def getRoute(self):
        return self.route

    def getMaterial(self):
        return self.material

    def getAmount(self):
        return self.amount

    # Set
    def setRoute(self, route):
        self.route = route

    def setMaterial(self, material):
        self.material = material

    def setAmount(self, amount):
        self.amount = amount
