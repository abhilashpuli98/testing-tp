# Last Updated: 2/5/2026, 9:25:25 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        n=len(nums)
        freqDict={}
        k=0
        for num in (nums):
            freqDict[num]=freqDict.get(num,0)+1
            if freqDict[num]<=2:
                nums[k]=num
                k+=1
        return k
        