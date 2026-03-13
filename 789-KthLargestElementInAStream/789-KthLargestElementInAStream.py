# Last Updated: 3/13/2026, 10:09:57 AM
class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k;
        self.nums=nums;
        heapq.heapify(self.nums)
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums);
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        heapq.heappush(self.nums,val);
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums);
        return self.nums[0]
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)