# Last Updated: 3/13/2026, 10:08:22 AM
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[:k])-sum(nums[-1:-k-1:-1]))