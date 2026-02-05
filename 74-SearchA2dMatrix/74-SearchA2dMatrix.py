# Last Updated: 2/5/2026, 9:25:32 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen=len(matrix)
        colLen=len(matrix[0])
        low,high=0,rowLen*colLen-1
        while low<=high:
            mid=(low+high)//2
            row=mid//colLen
            col=mid%colLen
            if matrix[row][col]==target:
                return True
            if matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False

        