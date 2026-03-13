# Last Updated: 3/13/2026, 10:09:52 AM
class Solution:
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        maxi=0
        left=0
        for i in range(1,len(binary)):
            if binary[i]=='1':
                maxi=max(maxi,abs(left-i))
                left=i
        return maxi 
