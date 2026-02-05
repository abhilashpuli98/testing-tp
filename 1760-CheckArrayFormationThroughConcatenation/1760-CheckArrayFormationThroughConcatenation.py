# Last Updated: 2/5/2026, 9:22:04 AM
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp={sm[0]:sm for sm in pieces}
        new=[]
        for i in range(len(arr)):
            new+=mp.get(arr[i],[])
        return new==arr