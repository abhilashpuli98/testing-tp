# Last Updated: 3/13/2026, 10:10:15 AM
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8:
            return []
        result=[]
        for hr in range(12):
            for mins in range(60):
                if hr.bit_count()+mins.bit_count()==turnedOn:
                    result.append(f'{hr}:{mins:02d}')
        return result