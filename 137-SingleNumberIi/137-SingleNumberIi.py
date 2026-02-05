# Last Updated: 2/5/2026, 9:24:53 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result=[]
        finalres=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and nums[i] not in result:
                result.append(nums[i])
        for i in range(len(nums)):
            result.append(nums[i])
        for i in range(len(result)):
            finalres^=result[i]
        return finalres