# Last Updated: 2/5/2026, 9:22:45 AM
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        result=[0,1]
        for i in range(2,n+1):
            temp=sum(result)
            result[0],result[1]=result[1],temp
        return result[-1]