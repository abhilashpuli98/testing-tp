# Last Updated: 3/13/2026, 10:09:00 AM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result=[]
        potions.sort()
        for s in spells:
            index=len(potions)
            l,r=0,len(potions)-1
            while l<=r:
                mid=(l+r)//2
                if s*potions[mid]>=success:
                    r=mid-1
                    index=mid
                else:
                    l=mid+1 #i forgot to sub add +1,-1 from mid i became mad and set r-=1,l+=1
            result.append(len(potions)-index)
        return result