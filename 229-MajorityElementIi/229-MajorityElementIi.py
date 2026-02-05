# Last Updated: 2/5/2026, 9:24:09 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1=None
        candidate2=None
        vote1,vote2=0,0
        res=[]
        for num in nums:
            if num==candidate1:
                vote1+=1
            elif num==candidate2:
                vote2+=1
            elif vote1==0:
                candidate1=num
                vote1=1
            elif vote2==0:
                vote2=1
                candidate2=num
            else:
                vote1-=1
                vote2-=1
        threshold=len(nums)//3
        if nums.count(candidate1)>threshold:
            res.append(candidate1)
        if nums.count(candidate2)>threshold:
            res.append(candidate2)
        return res