# Last Updated: 2/5/2026, 9:21:22 AM
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequency = Counter(power)
        keys = sorted(frequency)
        n=len(keys)
        dp = [0]*n
        dp[0] = frequency[keys[0]] * keys[0]
        for i in range(1,n):
            damageIfPicked = frequency[keys[i]] * keys[i]
            left,right,indx = 0,i-1 ,-1
            while left <= right:
                mid = (left+right)//2
                if keys[mid] <= keys[i]-3:
                    indx=mid
                    left=mid+1
                else:
                    right = mid-1
            if indx>=0:
                damageIfPicked+=dp[indx]
            dp[i] = max(dp[i-1],damageIfPicked)
        return dp[-1]