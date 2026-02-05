# Last Updated: 2/5/2026, 9:25:43 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
