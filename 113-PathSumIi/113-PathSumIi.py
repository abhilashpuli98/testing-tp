# Last Updated: 2/5/2026, 9:25:06 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result=[]
        def helper(node,reqSum,path):
            path.append(node.val)
            if not node.left and not node.right and reqSum==node.val:
                result.append(path[::])
                path.pop()
                return
            if node.left:
                helper(node.left,reqSum-node.val,path)
            if node.right:
                helper(node.right,reqSum-node.val,path)
            path.pop()
        helper(root,targetSum,[])
        return result

