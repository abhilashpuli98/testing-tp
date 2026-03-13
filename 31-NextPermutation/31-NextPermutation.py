# Last Updated: 3/13/2026, 10:11:28 AM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        indx=-1
        for i in range(n-1,-1,-1):
            if nums[i]<nums[i+1]:
                indx=i
                break
        if indx==-1:
            nums.reverse()
            return
        for i in range(n,indx,-1):
            if nums[indx]<nums[i]:
                nums[indx],nums[i]=nums[i],nums[indx]
                break
        nums[indx+1:]=reversed(nums[indx+1:])

        