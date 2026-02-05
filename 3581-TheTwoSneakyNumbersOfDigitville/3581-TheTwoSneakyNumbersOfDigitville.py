# Last Updated: 2/5/2026, 9:21:12 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq=[0]*len(nums)
        res=[]
        for num in nums:
            if freq[num]==1:
                res.append(num)
            else:
                freq[num]+=1
        return res 
