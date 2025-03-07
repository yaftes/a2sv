class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        stack = []
        while self.queue:
            stack.append(self.queue.pop())
        self.queue.append(x)
        while stack:
            self.queue.append(stack.pop())
        return 

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()
        return
        

    def peek(self) -> int:
        if self.queue:
            return self.queue[-1]
        return 

        

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()