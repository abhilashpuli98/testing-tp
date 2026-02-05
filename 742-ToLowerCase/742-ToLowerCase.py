# Last Updated: 2/5/2026, 9:23:01 AM
class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for letter in s:
            if 'A'<=letter<='Z':
                result+=chr(ord(letter)+32)
            else:
                result+=letter
        return result
        