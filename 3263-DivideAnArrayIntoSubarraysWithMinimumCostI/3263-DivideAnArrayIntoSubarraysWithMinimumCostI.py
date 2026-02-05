# Last Updated: 2/5/2026, 9:21:27 AM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        r=sorted(nums[1:])
        return r[0]+r[1]+nums[0]
        