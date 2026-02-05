# Last Updated: 2/5/2026, 9:23:45 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1.intersection(nums2))
        