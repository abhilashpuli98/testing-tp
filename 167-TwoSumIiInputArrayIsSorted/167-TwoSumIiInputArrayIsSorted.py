# Last Updated: 2/5/2026, 9:24:39 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Approach-1:#brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i+1,j+1]
        #Time Limit Exceeded T(n)=O(n^2) and S(n)=O(1) and 9 Mins"""
        """Approach-2:for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            req=target-nums[i]
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==req:
                    return [i+1,high+1]
                elif nums[mid]>req:
                    high=mid-1
                else:
                    low=mid+1"""
        """Approach-3:Best But S(n)=O(n)
        seen={}
        for i,val in enumerate(nums):
            difference=target-val
            if difference in seen:
                return [seen[difference]+1,i+1]
            seen[val]=i"""
        #Approach-4(Optimal):
        left=0
        right=len(nums)-1
        while(left<right):
            if (nums[left]+nums[right])==target:
                return [left+1,right+1]
            elif (nums[left]+nums[right])>target:
                right-=1
            else:
                left+=1