class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh_count += 1
                
        if fresh_count == 0: return 0

        time = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue and fresh_count > 0:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr,nc))


        return time if fresh_count == 0 else -1





















        # row, col = len(grid), len(grid[0])
        # queue = deque()
        # fresh = 0

        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == 2:
        #             queue.append([i, j])
        #         elif grid[i][j] == 1:
        #             fresh += 1
        
        # time = 0
        # direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # while queue and fresh > 0:

        #     level_size = len(queue)

        #     for i in range(level_size):
        #         r, c = queue.popleft()  # rotten orange

        #         for dr, dc in direct:
        #             new_r = r + dr
        #             new_c = c + dc

        #             if new_r >= 0 and new_r < row and new_c >= 0 and new_c < col and grid[new_r][new_c] == 1:
        #                 grid[new_r][new_c] = 2
        #                 fresh -= 1
        #                 queue.append([new_r, new_c])

        #     time += 1

        # if fresh == 0:
        #     return time

        # return -1











