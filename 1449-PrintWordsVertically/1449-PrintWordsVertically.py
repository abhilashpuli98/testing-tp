# Last Updated: 2/5/2026, 9:22:20 AM
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        result=[]
        max_length=max(len(word) for word in words)
        for i in range(max_length):
            current_word=""
            for j in range(len(words)):
                if i<len(words[j]):
                    current_word+=words[j][i]
                else:
                    current_word+=" "
            result.append(current_word.rstrip())
        return result
       
            