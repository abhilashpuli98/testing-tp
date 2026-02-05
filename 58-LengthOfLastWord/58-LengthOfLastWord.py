# Last Updated: 2/5/2026, 9:25:41 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(list(s.split())[-1])
        n=len(s)
        pointer=n-1
        count=0
        while s[pointer]==" ":
            pointer-=1
        while pointer<n and pointer>=0 and s[pointer]!=" ":
            count+=1
            pointer-=1
        return count