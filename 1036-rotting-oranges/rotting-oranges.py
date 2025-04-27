
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
     
        rows, cols = len(grid), len(grid[0])
        fresh = set()
        rotten = deque()  
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not fresh:
            return 0

        minutes = 0
     
        while rotten:
            size = len(rotten) 
            for _ in range(size):
                r, c = rotten.popleft()
               
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in fresh:
                        fresh.remove((nr, nc)) 
                        rotten.append((nr, nc))  
            if rotten:
                minutes += 1

        return -1 if fresh else minutes
