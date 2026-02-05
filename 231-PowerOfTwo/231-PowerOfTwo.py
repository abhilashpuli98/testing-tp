# Last Updated: 2/5/2026, 9:24:08 AM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&-n)==n