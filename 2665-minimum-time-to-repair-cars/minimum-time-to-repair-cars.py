class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, ranks[0] * cars * cars 
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            val = self.numberOfcars(ranks, mid)
            if val >= cars:
                result = mid
                right = mid - 1  
            else:
                left = mid + 1
        return result

    def numberOfcars(self, ranks, minute):
        total_car = 0
        for i in range(len(ranks)):
            total_car += int((minute / ranks[i]) ** 0.5)
        return total_car

   
        
        