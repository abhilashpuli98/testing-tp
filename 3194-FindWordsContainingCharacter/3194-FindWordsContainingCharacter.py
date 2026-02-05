# Last Updated: 2/5/2026, 9:21:33 AM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,word in enumerate(words) if x in word]