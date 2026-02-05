# Last Updated: 2/5/2026, 9:26:08 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        for right in range(1,len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
            #right+=1
        return left+1
