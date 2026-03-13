# Last Updated: 3/13/2026, 10:09:22 AM
class Solution:
    def check(self, nums: List[int]) -> bool:
        countBreaks=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                countBreaks+=1
            if countBreaks>1:
                return False
        if nums[0]<nums[-1]:
            countBreaks+=1
        return countBreaks<=1