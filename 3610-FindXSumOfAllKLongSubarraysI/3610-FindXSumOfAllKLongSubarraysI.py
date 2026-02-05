# Last Updated: 2/5/2026, 9:21:10 AM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result=[]
        for i in range(len(nums)-k+1):
            sub_arr=nums[i:i+k]
            freq=sorted(Counter(sub_arr).items() , key=lambda x: (x[1],x[0]) , reverse=True)[:x]
            temp=sum([j[1]*j[0] for j in freq])
            result.append(temp)
        return result
            