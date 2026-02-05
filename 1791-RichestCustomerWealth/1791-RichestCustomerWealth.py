# Last Updated: 2/5/2026, 9:22:09 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0
        for i in range(len(accounts)):
            result=max(result,sum(accounts[i][::]))
        return result