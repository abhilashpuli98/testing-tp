# Last Updated: 3/13/2026, 10:08:51 AM
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    res=max(res,nums[i]^nums[j])
        return res
