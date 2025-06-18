class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        possible_values = []
        index = 0

        for row in grid:
            row.sort(reverse=True)
            possible_values.extend(row[:limits[index]])
            index += 1

        heap = []
        for ele in possible_values:
            heapq.heappush(heap,-ele)

        total = 0
        for _ in range(k):
            total += -(heapq.heappop(heap))
            
        return total

        
        