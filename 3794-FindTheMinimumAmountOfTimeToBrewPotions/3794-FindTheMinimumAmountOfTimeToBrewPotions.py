# Last Updated: 2/5/2026, 9:20:49 AM
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n,m=len(skill),len(mana)
        done = [0]*n
        for val in mana:
            done[0] = done[0]+skill[0]*val
            for k in range(1,n):
                done[k] = max(done[k-1],done[k])+skill[k]*val
            for j in range(n-2,-1,-1):
                done[j] = done[j+1] - skill[j+1]*val
        return done[-1]