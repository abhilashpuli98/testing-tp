# Last Updated: 2/5/2026, 9:20:36 AM
class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        banterisol = (nums, s)

        heap = []
        score = 0
        ones_used = 0

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

            if s[i] == '1':
                score += -heapq.heappop(heap)
                ones_used += 1

        return score
