# Last Updated: 2/5/2026, 9:21:46 AM
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
       freq=Counter(num%value for num in nums)
       for i in range(len(nums)+1):
        if freq[i%value]==0:
            return i
        freq[i%value]-=1 