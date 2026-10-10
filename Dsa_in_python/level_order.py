from collections import deque
class Solution(object):
    def levelOrder(self, root):
        arr=[]
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            arr.append(level)
        return arr