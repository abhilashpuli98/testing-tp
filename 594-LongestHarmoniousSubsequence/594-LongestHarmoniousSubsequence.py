# Last Updated: 2/5/2026, 9:23:14 AM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq=Counter(nums)
        maxi=0
        for num in nums:
            if num+1 in freq:
                maxi=max(maxi,freq[num]+freq[num+1])
        return maxi