# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxNum):
            if not root:
                return 0
            good = 1 if root.val >= maxNum else 0

            maxNum = max(maxNum, root.val)

            good += dfs(root.left, maxNum)
            good += dfs(root.right, maxNum)

            return good
        
        return dfs(root, root.val)