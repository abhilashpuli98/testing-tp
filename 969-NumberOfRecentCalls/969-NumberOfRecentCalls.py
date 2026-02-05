# Last Updated: 2/5/2026, 9:22:48 AM
class RecentCounter:

    def __init__(self):
        self.records=[]
        self.exclusiveCount=0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[0]<t-3000:
            self.records.pop(0)
        return len(self.records)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)