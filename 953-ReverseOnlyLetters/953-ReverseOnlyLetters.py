# Last Updated: 2/5/2026, 9:22:49 AM
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if not (('a'<=s[left]<='z') or ('A'<=s[left]<='Z')):
                left+=1
                continue
            if not s[right].isalpha():
                right-=1
                continue
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return "".join(s)
        