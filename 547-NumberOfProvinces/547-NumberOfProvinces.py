# Last Updated: 2/5/2026, 9:23:16 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j]=True
                    dfs(j)
        n=len(isConnected)
        visited=[False]*n
        count=0
        for i in range(len(isConnected)):
            if not visited[i]:
                count+=1
                visited[i]=True
                dfs(i)
        return count
        #TRy bfs