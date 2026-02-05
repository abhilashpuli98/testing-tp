# Last Updated: 2/5/2026, 9:21:29 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        freq=list(freq.values())
        maxi=max(freq)
        result=0
        result= sum( maxi for fv in freq if maxi == fv)
        return result
        #TC(total)=O(n)+O(k)+O(NlogN)->(reduced) O(n)+O(2k)
        #SC=O(k)
            
        