# Last Updated: 2/5/2026, 9:23:49 AM
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num):
            count = 0
            for i in range(32):
                if (num>>i)&1:
                    count+=1
            return count
        bitArr = []
        for i in range(n+1):
            bitArr.append(count_ones(i))
        return bitArr

        