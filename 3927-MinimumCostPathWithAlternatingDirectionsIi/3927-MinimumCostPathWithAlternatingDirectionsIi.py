# Last Updated: 2/5/2026, 9:20:40 AM
import heapq

class Solution:
    def minCost(self, m: int, n: int, waitCost: list[list[int]]) -> int:
        heap=[(1,0,0,1)]
        visited={}
        while heap:
            cost,i,j,t=heapq.heappop(heap)
            if (i,j,t%2) in visited and visited[(i,j,t%2)]<=cost:
                continue
            visited[(i,j,t%2)]=cost
            if i==m-1 and j==n-1:
                return cost
            if t%2==1:
                for dx,dy in [(0,1),(1,0)]:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<m and 0<=nj<n:
                        entry_cost=(ni+1)*(nj+1)
                        heapq.heappush(heap,(cost+entry_cost,ni,nj,t+1))
            else:
                wait=waitCost[i][j]
                heapq.heappush(heap,(cost+wait,i,j,t+1))
        return -1
