# Last Updated: 3/13/2026, 10:09:53 AM
class Solution:
    def lemonadeChange(self, bill: List[int]) -> bool:
        f5=t10=t20=0
        for i in range(len(bill)):
            if bill[i]==5:
                f5+=5
            if bill[i]==10:
                if f5==0:
                    return False
                f5-=5
                t10+=10
            if bill[i]==20:
                if f5>0 and t10>0:
                    f5-=5
                    t10-=10
                elif f5>=15:
                    f5-=15
                else:
                    return False
        return True