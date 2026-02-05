# Last Updated: 2/5/2026, 9:21:05 AM
class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            bi=str(bin(n))[2:]
            if '0' not in bi:
                return n
            else:
                n+=1
