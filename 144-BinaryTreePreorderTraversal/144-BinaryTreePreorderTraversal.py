# Last Updated: 2/5/2026, 9:24:49 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        def preorder(root):
            if root is None:
                return
            output.append(root.val)
            left=preorder(root.left)
            right=preorder(root.right)
        preorder(root)
        return output