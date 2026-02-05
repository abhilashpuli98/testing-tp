# Last Updated: 2/5/2026, 9:25:17 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Cpd
class Solution:
    def ismirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.ismirror(left.left, right.right) and self.ismirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.ismirror(root.left, root.right)