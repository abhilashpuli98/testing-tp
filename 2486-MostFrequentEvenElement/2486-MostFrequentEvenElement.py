# Last Updated: 3/13/2026, 10:08:58 AM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num%2==0:
                freq[num] = freq.get(num,0)+1
        if not freq:
            return -1
        maxfreq=max(freq.values())
        return min(x for x in freq if freq[x]==maxfreq)