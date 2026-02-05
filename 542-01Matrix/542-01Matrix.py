# Last Updated: 2/5/2026, 9:23:18 AM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return 
        queue=deque()
        m,n=len(mat),len(mat[0])
        distance=[[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] is 0:
                    distance[i][j]=0
                    queue.append((i,j))
        dist=[[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            row,col=queue.popleft()
            for x,y in dist:
                nr,nc=x+row,y+col
                if 0<=nr<m and 0<=nc<n and distance[nr][nc]>distance[row][col]+1:
                    distance[nr][nc]=distance[row][col]+1
                    queue.append((nr,nc))
        return distance