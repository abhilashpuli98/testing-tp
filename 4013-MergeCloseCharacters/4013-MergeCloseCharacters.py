# Last Updated: 3/13/2026, 10:08:25 AM
class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s=list(s)
        while True:
            merged=False
            for i in range(len(s)):
                for j in range(i+1,min(len(s),i+k+1)):
                    if s[i]==s[j]:
                        s.pop(j)
                        merged=True
                        break
                if merged:
                    break
            if not merged:
                break
        return "".join(s)