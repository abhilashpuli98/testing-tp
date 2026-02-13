# Last Updated: 2/13/2026, 10:01:44 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n==0:
                return True
            if flowerbed[i]==0:
                isLeftEmpty = (i==0 or flowerbed[i-1]==0)
                isRightEmpty = (i==len(flowerbed)-1 or flowerbed[i+1]==0)
                if isLeftEmpty and isRightEmpty:
                    n-=1
                    flowerbed[i]=1
        return n==0