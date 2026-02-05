# Last Updated: 2/5/2026, 9:22:59 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result=None
        low,high=0,len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if letters[mid]>target:
                high=mid-1
                result=letters[mid]
            else:
                low=mid+1
        return result if result else letters[0]
        