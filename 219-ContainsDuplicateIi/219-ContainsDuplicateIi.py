# Last Updated: 2/5/2026, 9:24:12 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i,val in enumerate(nums):
                if val in seen and i-seen[val]<=k:
                    return True
                else:
                    seen[val]=i
        return False