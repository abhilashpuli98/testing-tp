# Last Updated: 2/5/2026, 9:22:18 AM
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    