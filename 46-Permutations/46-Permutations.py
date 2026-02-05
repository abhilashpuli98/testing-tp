# Last Updated: 2/5/2026, 9:25:54 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permu=[]
        result=[]
        def backtrack():
            if len(permu)==len(nums):
                result.append(permu[:])
                return
            for num in nums:
                if num not in permu:
                    permu.append(num)
                    backtrack()
                    permu.pop()

        backtrack()
        return result

        