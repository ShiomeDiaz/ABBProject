from Controller.ABBController import *
from Model.node import *
from Model.Mine import *


cavern1 = Mine(20, 'silver', 100)
cavern2 = Mine(80, 'gold', 100)
cavern3 = Mine(10, 'wood', 100)
cavern4 = Mine(50, 'rock', 100)
cavern5 = Mine(15, 'bronze', 100)
cavern6 = Mine(120, 'silver', 100)
cavern7 = Mine(44, 'rock', 100)

nod1 = Node(cavern1)
nod2 = Node(cavern2)
nod3 = Node(cavern3)
nod4 = Node(cavern4)
nod5 = Node(cavern5)
nod6 = Node(cavern6)
nod7 = Node(cavern7)

arbol = ABB()
arbol.add(nod1)
arbol.add(nod2)
arbol.add(nod3)
arbol.add(nod4)
arbol.add(nod5)
arbol.add(nod6)
arbol.add(nod7)


print("Inorder:", arbol.inOrder(nod1, []))