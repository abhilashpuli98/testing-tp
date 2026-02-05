# Last Updated: 2/5/2026, 9:24:30 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        result=""
        for i in range(32):
            result+='1' if (n>>i)&1 else '0'
        return int(result,2)