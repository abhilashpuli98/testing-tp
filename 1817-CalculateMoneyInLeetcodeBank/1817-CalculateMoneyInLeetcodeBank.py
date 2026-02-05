# Last Updated: 2/5/2026, 9:22:00 AM
class Solution:
    def totalMoney(self, n: int) -> int:
        """q,r=divmod(n,7)
        return (28*q)+(7*(q*(q-1)//2))+(r*(2*q+r+1))//2
        |-> short hand"""
        def calculateAmt(days,currWeek):
            total=0
            incr=currWeek
            return sum([currWeek+i for i in range(days)])
            """for _ in range(days):
                total+=incr
                incr+=1
            return total"""
        weeks,days=divmod(n,7)
        res=sum(calculateAmt(7,week) for week in range(1,1+weeks))
        if days:
            res+=calculateAmt(days,weeks+1)
        return res


        