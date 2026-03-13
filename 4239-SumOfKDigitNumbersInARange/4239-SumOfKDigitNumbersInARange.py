# Last Updated: 3/13/2026, 10:08:18 AM
class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD=10**9+7
        m=r-l+1
        s=(l+r)*m//2
        p1=pow(m,k-1,MOD)
        p10=pow(10,k,MOD)
        inv9=pow(9,MOD-2,MOD)
        g=(p10-1)%MOD
        g=(g*inv9)%MOD
        a=(s*p1)%MOD
        a=(a*g)%MOD
        return a