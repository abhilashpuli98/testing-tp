# Last Updated: 2/5/2026, 9:24:13 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=set()
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq.add(nums[i])
        return False
