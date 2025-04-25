
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        r = 0
        
        for h in houses:
            pos = bisect_left(heaters, h)
            left = heaters[pos - 1] if pos > 0 else float('-inf')
            right = heaters[pos] if pos < len(heaters) else float('inf')
            
            d_left = abs(h - left) if left != float('-inf') else float('inf')
            d_right = abs(h - right) if right != float('inf') else float('inf')
            
            r = max(r, min(d_left, d_right))
        
        return r


    



        