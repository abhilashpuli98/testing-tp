# Last Updated: 2/5/2026, 9:22:42 AM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        peri=0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if (nums[i+2]+nums[i+1])>nums[i]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0