# Last Updated: 2/5/2026, 9:20:35 AM
class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def ops(k):
            return sum((x+k-1)//k for x in nums)
        l,r=1,max(nums)+len(nums)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if ops(mid)<=mid*mid:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans