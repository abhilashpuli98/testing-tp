# Last Updated: 2/5/2026, 9:23:08 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        maxi=float('-inf')
        left=0
        right=k-1
        while right<n:
            if left is 0:
                curr_sum=sum(nums[left:right+1])
            else:
                curr_sum+=nums[right]
            if maxi<curr_sum:
                maxi=curr_sum
            curr_sum-=nums[left]
            left+=1
            right+=1
        return maxi/k