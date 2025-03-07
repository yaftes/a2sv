class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.map = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.map[num] += 1
        if len(self.queue) > self.k:
            val = self.queue.popleft()
            self.map[val] -= 1
        if self.map[self.value] != self.k:
            return False
        return True
        
        
        
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)