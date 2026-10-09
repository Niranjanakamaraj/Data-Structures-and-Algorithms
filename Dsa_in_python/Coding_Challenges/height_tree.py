class Node:
    def height(root):
        if root is None:
            return 0
        l=height(root.left)
        r=height(root.right)
        return max(l,r)+1