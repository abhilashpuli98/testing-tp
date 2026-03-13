# Last Updated: 3/13/2026, 10:10:14 AM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen=set()
        leng=0
        for c in s:
            if c in seen:
                seen.remove(c)
                leng+=2
            else:
                seen.add(c)
        return leng+1 if seen else leng