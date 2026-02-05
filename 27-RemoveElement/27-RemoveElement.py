# Last Updated: 2/5/2026, 9:26:07 AM
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right=len(nums)-1
        left=0
        while left<=right:
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1
        return left
                