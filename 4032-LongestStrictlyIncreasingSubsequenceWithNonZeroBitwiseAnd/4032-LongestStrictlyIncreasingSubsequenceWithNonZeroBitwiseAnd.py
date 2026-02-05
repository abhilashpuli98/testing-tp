# Last Updated: 2/5/2026, 9:20:37 AM
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for b in range(31):
            tails=[]
            for x in nums:
                if(x>>b)&1:
                    pos=bisect_left(tails,x)
                    if pos==len(tails):
                        tails.append(x)
                    else:
                        tails[pos]=x
                    ans=max(ans,len(tails))
        return ans