# Last Updated: 2/5/2026, 9:23:23 AM
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from collections import defaultdict
        max_heap=[]
        min_heap=[]
        #push the element w.r.t condts
        #simulataneous check
        #check condts and pop element 
        #check window range unwanted should be poped out
        n=len(nums)
        result=[]
        heap_dict=defaultdict(int)
        for i in range(k):
            heapq.heappush(max_heap,-nums[i])
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
            if len(max_heap)<len(min_heap):
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
        if k%2==1:
            result.append(-max_heap[0])
        else:
            result.append((-max_heap[0]+min_heap[0])/2)
        for i in range(k,n):
            previous_num=nums[i-k]
            heap_dict[previous_num]+=1
            balance = -1 if previous_num<=result[-1] else 1
            if nums[i]<=result[-1]:
                balance+=1
                heapq.heappush(max_heap,-nums[i])
            else:
                balance-=1
                heapq.heappush(min_heap,nums[i])
            if balance<0:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            elif balance>0:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
            while max_heap and heap_dict[-max_heap[0]]>0:
                heap_dict[-max_heap[0]]-=1
                heapq.heappop(max_heap)
            while min_heap and heap_dict[min_heap[0]]>0:
                heap_dict[min_heap[0]]-=1
                heapq.heappop(min_heap)
            
            if k%2==1:
                result.append(-max_heap[0])
            else:
                result.append((-max_heap[0]+min_heap[0])/2)
        return result
