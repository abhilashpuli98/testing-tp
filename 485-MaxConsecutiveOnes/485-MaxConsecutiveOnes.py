# Last Updated: 2/5/2026, 9:23:21 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for val in nums:
            if val==1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi