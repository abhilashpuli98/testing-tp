# Last Updated: 2/5/2026, 9:21:11 AM
class Solution:
    def kthCharacter(self, k: int) -> str:
        count=0
        res=['a']
        while len(res)<k:
            for i in range(len(res)):
                let=chr(ord('a')+((ord(res[i])-ord('a')+1)%26))
                res.append(let)
        return res[k-1]