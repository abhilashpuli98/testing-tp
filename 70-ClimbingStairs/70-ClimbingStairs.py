# Last Updated: 2/5/2026, 9:25:35 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a=[1,2]
        """for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        return a[-1]"""
        for i in range(2,n):
            a[0],a[1]=a[1],a[1]+a[0]
        return a[-1]
        #T(n)=O(n)
        #S(n)=O(n)
        