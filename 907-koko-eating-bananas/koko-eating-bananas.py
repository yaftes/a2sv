class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isFeasible(nums, k):
            count = 0
            for pile in nums:
                if pile <= k:
                    count += 1
                elif pile % k == 0:
                    count += (pile // k)
                else:
                    count += (pile // k) + 1
            return count 
        
        left, right = 1, max(piles)
        best = 0 

        while left <= right:
            mid = left + (right - left) // 2
            
            current = isFeasible(piles, mid)

            if current > h:
                left = mid + 1
            else:
                right = mid - 1
                best = mid  

        return best
        
            
        