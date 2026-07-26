class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1

            area += dfs(i, j+1)
            area += dfs(i, j-1)
            area += dfs(i+1, j)
            area += dfs(i-1, j)

            return area

        max_area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
        