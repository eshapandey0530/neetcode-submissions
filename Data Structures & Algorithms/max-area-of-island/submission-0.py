class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            count = 1

            count += dfs(i, j+1)
            count += dfs(i, j-1)
            count += dfs(i+1, j)
            count += dfs(i-1, j)

            return count

        max_count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_count = max(max_count, dfs(i, j))

        return max_count
        