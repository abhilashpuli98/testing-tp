# Last Updated: 3/13/2026, 10:09:16 AM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('0' if nums[i][i]=='1' else '1' for i in range(len(nums)))