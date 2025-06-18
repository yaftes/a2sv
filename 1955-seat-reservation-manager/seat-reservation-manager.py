class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1,n+1)]
        

    def reserve(self) -> int:
        smallest = heapq.heappop(self.heap)
        return smallest    

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)