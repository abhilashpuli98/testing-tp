# Last Updated: 2/5/2026, 9:25:50 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num,p):
            if not num:
                return 0
            if p==0:
                return 1
            result=helper(num,p//2)
            result*=result
            if p%2==1:
                return result*num
            return result
        result = helper(x,abs(n))
        if n<0:
            return 1/result
        return result