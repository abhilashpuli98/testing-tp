# Last Updated: 2/5/2026, 9:23:24 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0 or not grid[i][j] :
                return  1
            if grid[i][j]==-1:
                return 0
            grid[i][j]=-1
            #visited.add((i,j))
            return dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
        peri=0
        m,n=len(grid),len(grid[0])
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] :
                    return dfs(i,j)
                    
        return peri