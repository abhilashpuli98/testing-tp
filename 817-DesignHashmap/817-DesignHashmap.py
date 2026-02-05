# Last Updated: 2/5/2026, 9:22:54 AM
class MyHashMap:

    def __init__(self):
        self.HashMap=[None]*1000001

    def put(self, key: int, value: int) -> None:
        self.HashMap[key] = value

    def get(self, key: int) -> int:
        value = self.HashMap[key]
        return value if value is not None else -1

    def remove(self, key: int) -> None:
        self.HashMap[key]=None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)