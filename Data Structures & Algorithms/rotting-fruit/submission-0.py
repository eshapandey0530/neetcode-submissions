class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:

            level_size = len(queue)

            for i in range(level_size):
                r, c = queue.popleft()  # rotten orange

                for dr, dc in direct:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r >= 0 and new_r < row and new_c >= 0 and new_c < col and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue.append([new_r, new_c])

            time += 1

        if fresh == 0:
            return time

        return -1











