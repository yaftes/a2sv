class MapSum:

    def __init__(self):
        self.hash_map = {}
        

    def insert(self, key: str, val: int) -> None:
        self.hash_map[key] = val
        

    def sum(self, prefix: str) -> int:
        count = 0
        for key in self.hash_map:
            if key.startswith(prefix):
                count += self.hash_map[key]
        return count

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)