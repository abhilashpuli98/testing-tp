# Last Updated: 2/5/2026, 9:22:21 AM
class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        result=""
        for i in range(len(num)):
            if num[i]=="6":
                result+="9"+num[i+1:]
                return int(result)
            else:
                result+=num[i]
        return int(num)