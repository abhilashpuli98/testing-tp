# Last Updated: 2/5/2026, 9:44:04 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        index=0
        n=len(s)
        result=0
        while index<n and s[index]==' ':
            index+=1
        sign=1
        if index<n and (s[index]=='-' or s[index]=='+'):
            sign=-1 if s[index]=='-' else 1
            index+=1
        while index<n and '0'<=s[index]<='9':
            result=result*10+(ord(s[index])-ord('0'))
            if result<-2**31 or result>2**31-1:
                return 2**31-1 if sign==1 else -2**31
            index+=1
        return result*sign
