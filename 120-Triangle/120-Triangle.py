# Last Updated: 2/5/2026, 9:25:03 AM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for i,val in enumerate(row):
                dp[i]=val+min(dp[i],dp[i+1])
        return dp[0]