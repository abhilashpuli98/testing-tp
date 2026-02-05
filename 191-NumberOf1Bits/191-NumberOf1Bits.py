# Last Updated: 2/5/2026, 9:24:29 AM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            n=n&(n-1)
            count+=1
        return count