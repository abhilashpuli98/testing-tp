# Last Updated: 2/5/2026, 9:23:28 AM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)