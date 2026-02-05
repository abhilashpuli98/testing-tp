# Last Updated: 2/5/2026, 9:24:55 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res^=num
        return res