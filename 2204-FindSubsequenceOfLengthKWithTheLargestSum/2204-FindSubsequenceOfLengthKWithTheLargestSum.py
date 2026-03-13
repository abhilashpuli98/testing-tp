# Last Updated: 3/13/2026, 10:09:11 AM
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        topK=sorted(nums)[-k:]
        res=[]
        for i in range(len(nums)):
            if nums[i] in topK:
                res.append(nums[i])
                topK.remove(nums[i])
        return res