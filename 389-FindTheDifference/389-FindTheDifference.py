# Last Updated: 2/5/2026, 9:23:37 AM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for letter in s:
            result^=(ord(letter))
        for letter in t:
            result^=(ord(letter))
        return chr(result)
        