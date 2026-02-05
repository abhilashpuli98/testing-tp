# Last Updated: 2/5/2026, 9:40:39 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=float('-inf')
        left,right=0,len(height)-1
        while left<right:
            area=max(area,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area