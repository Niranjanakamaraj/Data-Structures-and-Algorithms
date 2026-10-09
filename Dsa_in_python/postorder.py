class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr=[]
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            arr.append(root.val)

        postorder(root)
        return arr