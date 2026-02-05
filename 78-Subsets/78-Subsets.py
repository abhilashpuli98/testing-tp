# Last Updated: 2/5/2026, 9:25:28 AM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        def dfs(start):
            result.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return result
        