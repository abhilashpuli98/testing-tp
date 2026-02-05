# Last Updated: 2/5/2026, 9:23:15 AM
class Solution:
    def checkRecord(self, s: str) -> bool:
        #a= 1 if s[0]=='A' else 0 
        a=0
        l=0
        prev=None
        for i in range(len(s)):
            if s[i] == 'A':
                a+=1
                if a>=2:
                    return False
            if s[i] == 'L' :
                l+=1
                if l>=3:
                    return False
            else:
                l=0
        return True
                
