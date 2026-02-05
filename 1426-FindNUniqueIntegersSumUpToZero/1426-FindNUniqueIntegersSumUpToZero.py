# Last Updated: 2/5/2026, 9:22:23 AM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        #return [-(n*(n-1))//2]+list(range(1,n))
        res=[]
        for i in range(1,(n//2)+1):
            res.append(i)
            res.append(-i)
        if n%2==1:
            res.append(0)
        return res
        
