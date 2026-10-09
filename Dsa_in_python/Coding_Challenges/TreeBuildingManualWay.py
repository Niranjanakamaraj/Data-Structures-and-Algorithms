class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)