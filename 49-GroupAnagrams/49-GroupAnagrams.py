# Last Updated: 2/5/2026, 9:25:51 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=dict()
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in result:
                result[sorted_word]=[]
            result[sorted_word].append(word)
        return list(result.values())