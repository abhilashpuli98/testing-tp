# Last Updated: 2/5/2026, 9:21:53 AM
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count!=3:
             return False
        return True


        