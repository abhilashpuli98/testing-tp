# Last Updated: 2/5/2026, 9:25:37 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        