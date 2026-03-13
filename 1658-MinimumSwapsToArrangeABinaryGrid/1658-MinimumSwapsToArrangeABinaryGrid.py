# Last Updated: 3/13/2026, 10:09:32 AM
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        trailingZeros=[]
        n=len(grid)
        requiredZeros=[]
        swaps=0
        for i in range(n):
            zerosCount=0
            for j in range(n-1,-1,-1):
                if grid[i][j]==0:
                    zerosCount+=1
                else:
                    break
            trailingZeros.append(zerosCount)
            requiredZeros.append(n-i-1)
        for i in range(n):
            j=i
            #stupid bug i Did i set j=i+1 which is a bug because
            # if i have sufficient no.of zeros and all bellow are alredy in crt positions
            #returns -1 so i have to check my current pos
            while j<n and trailingZeros[j]<requiredZeros[i]:
                j+=1
            if j==n:
                return -1
            while j>i:
                trailingZeros[j],trailingZeros[j-1]=trailingZeros[j-1],trailingZeros[i]
                swaps+=1
                j-=1
        return swaps
            