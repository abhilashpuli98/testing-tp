# Last Updated: 2/5/2026, 9:44:01 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return  str(x)==str(x)[::-1]