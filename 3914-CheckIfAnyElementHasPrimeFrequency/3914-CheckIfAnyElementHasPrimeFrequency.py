# Last Updated: 2/5/2026, 9:20:41 AM
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True   
        freq=dict()
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for val in freq.values():
            if is_prime(val):
                return True
        return False
            