# Last Updated: 3/13/2026, 10:09:20 AM
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        #return '01' not in s
        count=0
        segments=0
        for bit in s:
            if bit=='1':
                count+=1
            else:
                if count>0:
                    segments+=1
                count=0
                if segments>1:
                    return False
        if count:
            segments+=1
        return segments<=1