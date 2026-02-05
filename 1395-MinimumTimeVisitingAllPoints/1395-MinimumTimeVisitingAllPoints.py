# Last Updated: 2/5/2026, 9:22:27 AM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(p[0]-q[0]),abs(p[1]-q[1])) for p,q in pairwise(points))
        