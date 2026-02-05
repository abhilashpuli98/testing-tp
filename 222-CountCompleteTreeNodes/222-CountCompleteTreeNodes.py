# Last Updated: 2/5/2026, 9:24:11 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0
        def dfs(root):
            nonlocal count
            if not root:
                return
            count+=1
            root.left=dfs(root.left)
            root.right=dfs(root.right)
        dfs(root)
        return count
