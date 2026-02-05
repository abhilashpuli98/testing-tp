# Last Updated: 2/5/2026, 9:23:03 AM
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
        