# Last Updated: 2/5/2026, 9:21:00 AM
class Solution:
    def findValidPair(self, s: str) -> str:
        s = list(s)
        freq = Counter(s)
        for i in range(1,len(s)):
            if s[i-1]!=s[i] and int(s[i]) == freq[s[i]] and int(s[i-1])==freq[s[i-1]]:
                return s[i-1]+s[i]
        return ""