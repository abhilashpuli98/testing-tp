# Last Updated: 2/5/2026, 9:22:13 AM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sml=[]
        count=0
        for i in  nums:
            for j in nums:
                if j<i:
                    count=count+1
            sml.append(count)
            count=0
        return sml