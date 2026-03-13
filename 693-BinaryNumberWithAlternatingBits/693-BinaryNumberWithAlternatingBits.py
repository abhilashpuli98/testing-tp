# Last Updated: 3/13/2026, 10:10:01 AM
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n>>1)
        return x&(x+1)==0