# Last Updated: 3/13/2026, 10:09:10 AM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Approach -1 return [ i for i,ele in enumerate(sorted(nums)) if ele == target]
        freq = Counter(nums)
        lt_nums = sum([f for item,f in freq.items() if item<target])
        return list(range(lt_nums,freq[target]+lt_nums))