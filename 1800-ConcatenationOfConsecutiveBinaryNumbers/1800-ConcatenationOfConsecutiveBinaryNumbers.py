# Last Updated: 3/13/2026, 10:09:26 AM
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        biRep=""
        for i in range(1,n+1):
            biRep+=bin(i)[2:]
        return (int(biRep,2))%(10**9+7)
