# Last Updated: 2/5/2026, 9:21:58 AM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        resultant=0
        for opr in operations:
            if opr in ["++X","X++"]:
                resultant+=1
            else:
                resultant-=1
        return resultant