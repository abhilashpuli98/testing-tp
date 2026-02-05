# Last Updated: 2/5/2026, 9:23:07 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return is_palindrome(left+1,right) or is_palindrome(left,right-1)
            left+=1
            right-=1
        return True