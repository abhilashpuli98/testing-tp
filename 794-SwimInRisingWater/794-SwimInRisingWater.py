# Last Updated: 2/5/2026, 9:22:56 AM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited=set()
        visited.add((0,0))
        minHeap=[[grid[0][0],0,0]]

        while minHeap:
            time,row,col=heapq.heappop(minHeap)

            if row == N-1 and col == N-1:
                return time
            
            for drow,dcol in directions:
                neighRow,neighCol = row+drow,col+dcol

                if (neighRow==N or neighRow<0 or neighCol==N or neighCol<0 or ((neighRow,neighCol) in visited)):
                    continue
                visited.add((neighRow,neighCol))
                heapq.heappush(minHeap,[max(time,grid[neighRow][neighCol]),neighRow,neighCol])
                