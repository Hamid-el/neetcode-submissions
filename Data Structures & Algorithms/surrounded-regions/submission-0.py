class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):
            stack = [(row, col)]
            board[row][col] = "#"

            while stack:
                curr_row, curr_col = stack.pop()

                for row_change, col_change in directions:
                    next_row = curr_row + row_change
                    next_col = curr_col + col_change

                    if (next_row < 0 or next_row >= rows or
                        next_col < 0 or next_col >= cols or
                        board[next_row][next_col] != "O"):
                        continue

                    board[next_row][next_col] = "#"
                    stack.append((next_row, next_col))

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0) #left border

            if board[row][cols - 1] == "O":
                dfs(row, cols - 1) #right border

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col) # top border

            if board[rows - 1][col] == "O":
                dfs(rows - 1, col) # bottom border

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"