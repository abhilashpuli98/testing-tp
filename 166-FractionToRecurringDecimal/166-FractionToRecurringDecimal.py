# Last Updated: 2/5/2026, 9:24:40 AM
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n==0:
            return "0"
        result=[]
        if (n<0) ^ (d<0):
            result.append("-")
        n=abs(n)
        d=abs(d)
        result.append(str(n//d))
        reminder=n%d
        if reminder==0:
            return "".join(result)
        result.append(".")
        Map={}
        while reminder:
            if reminder in Map:
                pos=Map[reminder]
                result.insert(pos,"(")
                result.append(")")
                break
            Map[reminder]=len(result)
            result.append(str(reminder*10//d))
            reminder=reminder*10%d
        return "".join(result)

            

        
        