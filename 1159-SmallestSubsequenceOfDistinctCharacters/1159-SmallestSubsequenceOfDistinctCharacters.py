# Last Updated: 2/5/2026, 9:22:35 AM
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        seen=dict()
        freq=dict()
        for char in s:
            freq[char]=freq.get(char,0)+1
        for char in s:
            freq[char]-=1
            if seen.get(char,False):
                continue
            while stack and stack[-1]>char and freq[stack[-1]]>0:
                seen[stack[-1]]=False
                stack.pop()
            stack.append(char)
            seen[char]=True
        return ''.join(stack)