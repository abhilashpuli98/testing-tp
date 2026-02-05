# Last Updated: 2/5/2026, 9:22:38 AM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary=""
        for i in range(len(nums)):
            binary+=str(nums[i])
            if int(binary,2) %5 ==0:
                nums[i]=True
            else:
                nums[i]=False
        return nums
