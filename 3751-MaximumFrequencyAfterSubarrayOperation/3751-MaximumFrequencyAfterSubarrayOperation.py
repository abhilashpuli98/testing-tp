# Last Updated: 2/5/2026, 9:20:57 AM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        def kadane(x):
            res=cur=0
            for y in nums:
                if x == y:
                    cur+=1
                if y == k:
                    cur-=1
                if cur<0:
                    cur=0
                res = max(res,cur)
            return res
        result = max(kadane(x) for x in freq)
        return freq[k]+result