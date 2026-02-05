# Last Updated: 2/5/2026, 9:25:04 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        pRows=self.generate(numRows-1)
        prev=[1]*numRows
        for i in range(1,numRows-1):
            prev[i]=pRows[-1][i-1]+pRows[-1][i]
        pRows.append(prev)
        return pRows
