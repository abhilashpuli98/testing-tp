# Last Updated: 2/5/2026, 9:21:03 AM
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        result=[]
        if not grid:
            return result
        k=1
        for i in range(1,m+1):
            if i%2!=0:
                for j in range(1,n+1):
                    if k%2!=0 and i%2!=0:
                        result.append(grid[i-1][j-1])
                    elif j%2==0 and i%2==0:
                        result.append(grid[i-1][j-1])
                    k+=1
            elif i%2==0:
                for j in range(n,0,-1):
                    if k%2!=0 and i%2!=0:
                        result.append(grid[i-1][j-1])
                    elif j%2==0 and i%2==0:
                        result.append(grid[i-1][j-1])
                    k+=1
        return result

