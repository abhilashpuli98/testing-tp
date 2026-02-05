# Last Updated: 2/5/2026, 9:23:50 AM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 3**19%n==0