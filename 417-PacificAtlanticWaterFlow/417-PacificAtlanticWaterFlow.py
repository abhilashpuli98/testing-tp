# Last Updated: 2/5/2026, 9:23:30 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        atl,paci=set(),set()
        def dfs(r,c,prevHeight,visited):
            if r<0 or c<0 or r>=m  or c>=n or prevHeight>heights[r][c] or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r-1,c,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)
            dfs(r+1,c,heights[r][c],visited)
            dfs(r,c+1,heights[r][c],visited)
        for i in range(n):
            dfs(0,i,heights[0][i],paci)
            dfs(m-1,i,heights[m-1][i],atl)
        for j in range(m):
            dfs(j,0,heights[j][0],paci)
            dfs(j,n-1,heights[j][n-1],atl)
        result=list(atl.intersection(paci))
        return result

        