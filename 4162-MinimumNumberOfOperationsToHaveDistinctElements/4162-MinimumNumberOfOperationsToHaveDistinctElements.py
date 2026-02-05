# Last Updated: 2/5/2026, 9:20:32 AM
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)

        # count how many numbers currently have duplicates
        dupCount = 0
        for v in freq.values():
            if v >= 2:
                dupCount += 1

        if dupCount == 0:
            return 0

        ops = 0
        i = 0
        n = len(nums)

        while i < n:
            ops += 1

            # remove first three elements
            for _ in range(3):
                if i >= n:
                    break

                x = nums[i]
                freq[x] -= 1

                # if it just stopped being a duplicate
                if freq[x] == 1:
                    dupCount -= 1

                i += 1

            if dupCount == 0:
                return ops

        return ops