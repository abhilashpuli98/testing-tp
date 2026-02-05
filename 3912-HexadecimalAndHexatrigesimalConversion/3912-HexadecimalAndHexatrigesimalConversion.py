# Last Updated: 2/5/2026, 9:20:43 AM
class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base36(num,base):
            chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            base36=''
            while num>0:
                base36=chars[num%base]+base36
                num//=base
            return base36 or '0'
        def convert(n):
            h=to_base36(n*n,16)
            b=to_base36(n*n*n,36)
            return h+b
        return convert(n)