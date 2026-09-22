class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

curr = n1
while curr:
    print(curr.data, end=" ")
    curr = curr.next