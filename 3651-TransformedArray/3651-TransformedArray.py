# Last Updated: 2/5/2026, 9:32:47 PM
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        #return [nums[(i+shifts)%len(nums)] for i,shifts in enumerate(nums)]
        result=[]
        n=len(nums)
        for indx,num in enumerate(nums):
            if num>0:
                result.append(nums[(indx+num)%n])
            if num<0:
                result.append(nums[(indx+n-(abs(num)%n))%n])
            if nums[indx]==0:
                result.append(0)
        return result

