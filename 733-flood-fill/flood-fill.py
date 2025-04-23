class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        row_limit = len(image)
        col_limit = len(image[0])
        visited = set()
        def dfs(row,col):

            if row < 0 or col < 0 or row >= row_limit or col >= col_limit or start_color != image[row][col] or (row,col) in visited:
                return
            image[row][col] = color
            visited.add((row,col))
            dfs(row - 1,col)
            dfs(row + 1,col)
            dfs(row , col - 1)
            dfs(row , col + 1)
        dfs(sr,sc)
        return image


        