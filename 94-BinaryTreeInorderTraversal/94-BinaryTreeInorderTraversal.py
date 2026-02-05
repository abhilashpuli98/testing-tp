# Last Updated: 2/5/2026, 9:25:20 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        def inorder(root):
            if root is None:
                return
            left=inorder(root.left)
            output.append(root.val)
            right=inorder(root.right)
        inorder(root)
        return output

        