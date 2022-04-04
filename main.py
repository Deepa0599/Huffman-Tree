


class node :
    def __init__(self, frequency, sym, left=None, right=None):

        self.frequency = frequency


        self.sym = sym


        self.left = left


        self.right = right


        self.huff = ''




def printNodes(node, val=''):

    newVal = val + str(node.huff)


    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)


    if (not node.left and not node.right):
        print(f"{node.sym} -> {newVal}")



chars = ['w', 'A', 'e', 'r', 'i', 'n', 'o', 's', 'k']


frequency = [7, 21, 12, 8, 12, 30, 8, 5, 12]


nodes = []


for x in range(len(chars)):
    nodes.append(node(frequency[x], chars[x]))

while len(nodes) > 1:

    nodes = sorted(nodes, key=lambda x: x.frequency)


    left = nodes[0]
    right = nodes[1]


    left.huff = 0
    right.huff = 1


    newNode = node(left.frequency + right.frequency, left.sym + right.sym, left, right)


    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


printNodes(nodes[0])