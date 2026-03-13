# Last Updated: 3/13/2026, 10:09:48 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        low,high=0,len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[low])>abs(nums[high]):
                result[i]=nums[low]**2
                low+=1
            else:
                result[i]=nums[high]**2
                high-=1
        return result