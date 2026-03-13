# Last Updated: 3/13/2026, 10:08:59 AM
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        result = max(Counter(ranks).values())
        if result>2:
            return 'Three of a Kind'
        if result==2:
            return 'Pair'
        return 'High Card'