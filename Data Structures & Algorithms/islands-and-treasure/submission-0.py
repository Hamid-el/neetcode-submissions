class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        # Multi-source BFS
        while queue:
            curr_row, curr_col = queue.popleft()

            for row_change, col_change in directions:
                next_row = curr_row + row_change
                next_col = curr_col + col_change

                if (next_row < 0 or next_row >= rows or
                    next_col < 0 or next_col >= cols or
                    grid[next_row][next_col] != 2147483647):
                    continue

                grid[next_row][next_col] = grid[curr_row][curr_col] + 1
                queue.append((next_row, next_col))