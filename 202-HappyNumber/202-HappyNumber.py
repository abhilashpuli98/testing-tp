# Last Updated: 2/5/2026, 9:24:21 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        if n==1:
            return True
        while n!=1:
            n=sum([int(digit)**2 for digit in str(n)])
            if n in seen:
                return False
            seen.add(n)
        return True

        