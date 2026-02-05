# Last Updated: 2/5/2026, 9:24:14 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]