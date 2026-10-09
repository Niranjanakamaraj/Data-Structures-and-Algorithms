class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        return arr