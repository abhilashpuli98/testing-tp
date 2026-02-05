# Last Updated: 2/5/2026, 9:25:39 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """num="".join([str(digit) for digit in digits])
        num=str(int(num)+1)
        return [int(i) for i in num]"""
        carry=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits
        