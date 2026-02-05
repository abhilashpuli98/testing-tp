# Last Updated: 2/5/2026, 9:21:18 AM
class Solution:
    def getSmallestString(self, s: str) -> str:
        result=""
        def ord_cov(num):
            return ord(num)-ord('0')
        for i in range(1,len(s)):
            a=ord_cov(s[i-1])
            b=ord_cov(s[i])
            if a > b  and (a%2 == b%2 ):
                result+=s[i]+s[i-1]+ s[i+1:]
                return result
            result+=s[i-1]
        return s