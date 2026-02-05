# Last Updated: 2/5/2026, 9:24:59 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        substr=[]
        def backtrack(indx):
            if indx>=len(s):
                result.append(substr[:])
                return 
            for i in range(indx,len(s)):
                if self.is_palindrome(s,indx,i):
                    substr.append(s[indx:i+1])
                    backtrack(i+1)
                    substr.pop()
        backtrack(0)
        return result   
    def is_palindrome(self,s,i,j):
        left=i
        right=j
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True