# Last Updated: 3/13/2026, 10:09:04 AM
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        fullCap=0
        need=[]
        for i in range(len(capacity)):
            if capacity[i]==rocks[i]:
                fullCap+=1
            else:
                need.append(capacity[i]-rocks[i])
        if sum(need)<=additionalRocks:
            return len(need)+fullCap
        need.sort()
        for i in range(len(need)):
            if additionalRocks<need[i]:
                break
            additionalRocks-=need[i]
            fullCap+=1
        return fullCap