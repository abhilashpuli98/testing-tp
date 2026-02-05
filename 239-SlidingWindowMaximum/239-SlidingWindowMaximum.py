# Last Updated: 2/5/2026, 9:24:03 AM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq=deque()
        result=[]
        for i in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            if dq and dq[0]<=i-k:
                dq.popleft()
            dq.append(i)
            if i>=k-1:
                result.append(nums[dq[0]])
        return result
 #---------------------------------------------------------------------------------       
        """n=len(nums)
        if n==1 and k is 1 :
            return nums
        if k is 1:
            return nums
        left=0
        right=left+k-1
        while right<n:
            if left==0:
                nums[left]=max(nums[left:right+1])
            elif k>3:
                nums[left]=max(nums[left-1],nums[right])
            else:
                nums[left]=max(nums[left:right+1])
            left+=1
            right+=1
        return nums[:left]"""
        