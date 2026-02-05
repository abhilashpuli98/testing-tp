# Last Updated: 2/5/2026, 9:25:16 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        q=deque()
        if not root:
            return result
        q.append(root)
        while q:
            level=len(q)
            sublevel=[]
            while level:
                node=q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sublevel.append(node.val)
                level-=1  
            result.append(sublevel)
        return result