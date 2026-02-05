# Last Updated: 2/5/2026, 9:23:31 AM
import sys
sys.set_int_max_str_digits(6000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x=int(num1)
        y=int(num2)
        return str(x+y)
        