# Last Updated: 2/13/2026, 10:01:46 AM
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])