class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr=[]
        def p(root):
            if not root:
                return
            arr.append(root.val)
            p(root.left)
            p(root.right)
        p(root)
        return arr