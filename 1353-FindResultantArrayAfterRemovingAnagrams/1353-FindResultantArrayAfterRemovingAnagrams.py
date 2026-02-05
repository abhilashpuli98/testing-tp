# Last Updated: 2/5/2026, 9:22:28 AM
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[words[0]]
        result.extend([words[i] for i in range(1,len(words)) if sorted(words[i]) != sorted(words[i-1]) ])
        return result