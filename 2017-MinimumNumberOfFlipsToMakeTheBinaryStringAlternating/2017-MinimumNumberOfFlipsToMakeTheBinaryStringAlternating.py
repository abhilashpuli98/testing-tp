# Last Updated: 3/13/2026, 10:09:18 AM
class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s+=s
        alter1=''
        alter2=''
        for i in range(len(s)):
            alter1+= '0' if i%2==0 else '1'
            alter2+= '1' if i%2==0 else '0'
        differ1,differ2=0,0
        left=0
        res=float('inf')
        for r in range(len(s)):
            if s[r]!=alter1[r]:
                differ1+=1
            if s[r]!=alter2[r]:
                differ2+=1
            if (r-left+1)>n:
                if s[left]!=alter1[left]:
                    differ1-=1 #decrease the Differ if it contributed in current window
                if s[left]!=alter2[left]:
                    differ2-=1
                left+=1
            if (r-left+1)>=n:
                res=min(res,differ1,differ2)
        return res
