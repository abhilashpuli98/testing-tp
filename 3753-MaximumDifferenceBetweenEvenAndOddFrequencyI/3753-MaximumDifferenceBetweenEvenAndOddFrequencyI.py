# Last Updated: 2/5/2026, 9:20:56 AM
class Solution:
    def maxDifference(self, s: str) -> int:
        bucket=Counter(s)
        even=float('inf')
        odd=0
        for i in bucket:
            if bucket[i]%2!=0:
                odd=max(bucket[i],odd)
            if bucket[i]%2==0 :
                even=min(even,bucket[i])
        return odd-even
        
        