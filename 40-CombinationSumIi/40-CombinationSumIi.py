# Last Updated: 2/5/2026, 9:25:58 AM
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol=[]
        result=[]
        def backtrack(start,total):
            if total==target :
                result.append(sol[:])
                return
            if total>target:
                return
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sol.append(nums[i])
                backtrack(i+1,total+nums[i])
                sol.pop()
        backtrack(0,0)
        return result
        