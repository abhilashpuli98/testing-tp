# Last Updated: 2/5/2026, 9:21:14 AM
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result=0
        def count(s):
            o=z=0
            for x in s:
                if x=='1':
                    o+=1
                else:
                    z+=1
            return o,z
        for i in range(len(s)):
            for j in range(i,len(s)):
                ones,zeros= count(s[i:j+1])
                if ones<=k or zeros<=k:
                    result+=1
        return result
                