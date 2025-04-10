class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(r,c):

            if ((r,c) in visited or r >= row or c >= col or grid[r][c] == 0 or r < 0 or c < 0):
                return 0

            area = 1
            visited.add((r,c))

            area += dfs(r,c - 1)
            area += dfs(r,c + 1)
            area += dfs(r + 1,c)
            area += dfs(r - 1,c)

            return area

        max_val = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_val = max(max_val,dfs(r,c))
        return max_val
        
       




        
        