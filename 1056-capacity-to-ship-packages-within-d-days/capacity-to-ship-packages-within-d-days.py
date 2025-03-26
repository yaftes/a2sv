class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) 
        right = sum(weights) 
        best = -1
        while left <= right:
            mid = left + (right - left) // 2
            if self.capacityFinder(weights, mid) <= days:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best

    def capacityFinder(self, num, val):
        count = 1 
        tot = 0
        for ele in num:
            if ele > val:
                return float('inf') 
            if tot + ele <= val:
                tot += ele
            else:
                count += 1
                tot = ele
        return count