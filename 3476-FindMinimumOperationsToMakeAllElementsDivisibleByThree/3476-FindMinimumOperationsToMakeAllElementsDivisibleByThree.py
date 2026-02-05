# Last Updated: 2/5/2026, 9:21:19 AM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 for val in nums if val%3!=0])
