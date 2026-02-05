# Last Updated: 2/5/2026, 9:22:29 AM
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=0
        indx= None
        for i in range (0,len(arr)-2):
            if arr[i]%2!=0 and  arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
        return False 
            
                
        
            