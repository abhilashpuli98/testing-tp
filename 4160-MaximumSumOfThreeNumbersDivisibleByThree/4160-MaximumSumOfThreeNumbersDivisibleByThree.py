# Last Updated: 2/5/2026, 9:20:30 AM
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        malorivast = nums

        mod0, mod1, mod2 = [], [], []

        for x in malorivast:
            if x % 3 == 0:
                mod0.append(x)
            elif x % 3 == 1:
                mod1.append(x)
            else:
                mod2.append(x)

        mod0.sort(reverse=True)
        mod1.sort(reverse=True)
        mod2.sort(reverse=True)

        ans = 0

        # (0,0,0)
        if len(mod0) >= 3:
            ans = max(ans, mod0[0] + mod0[1] + mod0[2])

        # (1,1,1)
        if len(mod1) >= 3:
            ans = max(ans, mod1[0] + mod1[1] + mod1[2])

        # (2,2,2)
        if len(mod2) >= 3:
            ans = max(ans, mod2[0] + mod2[1] + mod2[2])

        # (0,1,2)
        if len(mod0) >= 1 and len(mod1) >= 1 and len(mod2) >= 1:
            ans = max(ans, mod0[0] + mod1[0] + mod2[0])

        return ans