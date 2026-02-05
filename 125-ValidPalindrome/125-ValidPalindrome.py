# Last Updated: 2/5/2026, 9:25:02 AM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        left,right=0,len(s)-1
        while left<right:
            if s[left].isalnum() and s[right].isalnum() and s[left]==s[right]:
                left+=1
                right-=1
            elif not(s[left].isalnum()) or not(s[right].isalnum()):
                if not(s[left].isalnum()):
                    left+=1
                if not(s[right].isalnum()):
                    right-=1
            elif s[left].isalnum() and s[right].isalnum() and s[left]!=s[right]:
                    return False
        return True


        