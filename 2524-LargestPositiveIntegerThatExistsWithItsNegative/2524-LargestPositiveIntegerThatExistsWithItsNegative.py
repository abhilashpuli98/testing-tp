# Last Updated: 3/13/2026, 10:08:57 AM
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen=set(nums)
        result=0
        for num in nums:
            if num>result and -num in seen:
                result=num
        return result if result!=0 else -1