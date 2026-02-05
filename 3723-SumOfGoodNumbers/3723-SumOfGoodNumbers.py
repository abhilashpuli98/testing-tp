# Last Updated: 2/5/2026, 9:21:01 AM
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result=0
        n=len(nums)
        for i in range(len(nums)):
            left = i-k>=0
            right =i+k<n
            if left and right:
                if nums[i]>nums[i+k] and nums[i]>nums[i-k]:
                    result+=nums[i]
            elif right:
                if nums[i]>nums[i+k] :
                    result+=nums[i]
            elif left:
                if nums[i]>nums[i-k]:
                    result+=nums[i]
        return result
            
        