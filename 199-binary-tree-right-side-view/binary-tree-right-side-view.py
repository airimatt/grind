# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        queue = collections.deque([root])

        while queue:
            length = len(queue)
            rightside = None
            for i in range(length):
                node = queue.popleft()
                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightside:
                res.append(rightside.val)
        
        return res


        # def bfs(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     if root.left and not root.right:
        #         bfs(root.left)
        #     bfs(root.right)
        
        # bfs(root)
        
        # return res
    
        
        