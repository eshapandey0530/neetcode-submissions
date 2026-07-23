class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            hset = set()
            for j in range(cols):
                if board[i][j] in hset:
                    return False
                elif board[i][j] != '.':
                    hset.add(board[i][j])

        for i in range(rows):
            hset = set()
            for j in range(cols):
                if board[j][i] in hset:
                    return False
                elif board[j][i] != '.':
                    hset.add(board[j][i])

        directions = [(0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)]

        for i, j in directions:
            hset = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in hset:
                        return False
                    elif board[row][col] != '.':
                        hset.add(board[row][col])

        return True





