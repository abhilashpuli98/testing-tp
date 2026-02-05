# Last Updated: 2/5/2026, 9:24:24 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        count=0
        def dfs(start,end):
            if not (0<=start<rows and 0<=end<cols) or grid[start][end]!='1' or (start,end) in visited:
                return
            visited.add((start,end))
            dfs(start+1,end)
            dfs(start-1,end)
            dfs(start,end+1)
            dfs(start,end-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count
        