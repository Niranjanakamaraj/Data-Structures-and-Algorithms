class Node:
    def __init__ (self,value):
        self.data=value
        self.left=None
        self.right=None
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)
node=Node(10)
node.left=Node(20)
node.right=Node(30)
node.left.left=Node(40)
node.left.right=Node(50)
preorder(node)