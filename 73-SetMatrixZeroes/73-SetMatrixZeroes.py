# Last Updated: 2/5/2026, 9:25:34 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        s1=set()
        for i in range(row):
            left=0
            right=col-1
            while left<=right:
                if matrix[i][left]==0:
                    s1.add((i,left))
                if matrix[i][right]==0:
                    s1.add((i,right))
                left+=1
                right-=1
        for r, c in s1:
            matrix[r] = [0] * len(matrix[0])     
            for i in range(len(matrix)):         
                matrix[i][c] = 0


                