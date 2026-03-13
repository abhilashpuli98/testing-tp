# Last Updated: 3/13/2026, 10:08:20 AM
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counter=Counter(nums)
        values=sorted(counter.keys())
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                if counter[values[i]]!=counter[values[j]]:
                    return [values[i],values[j]]
        return [-1,-1]