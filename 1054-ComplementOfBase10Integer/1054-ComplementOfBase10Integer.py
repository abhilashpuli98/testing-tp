# Last Updated: 2/5/2026, 9:22:41 AM
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """res=""
        bits=bin(n)[2:]
        for bit in bits:
            if bit=='0':
                res+='1'
            else:
                res+='0'
        return int(res,2)"""
        
        return 1 if n==0 else ((1<<n.bit_length())-1)^n