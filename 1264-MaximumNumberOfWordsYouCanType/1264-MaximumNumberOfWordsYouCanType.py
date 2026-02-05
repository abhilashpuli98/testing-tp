# Last Updated: 2/5/2026, 9:22:31 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split(" ")
        count=0
        for word in words:
            isrep=True
            for letter in brokenLetters:
                if letter in word:
                    isrep=False
            if isrep:
                count+=1
        return count