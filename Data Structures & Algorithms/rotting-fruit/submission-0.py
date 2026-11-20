class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                
        # BFS
        while queue  and fresh > 0:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                for row_change, col_change in directions:
                    next_row = curr_row + row_change
                    next_col = curr_col + col_change

                    if (next_row < 0 or next_row >= rows or
                        next_col < 0 or next_col >= cols or
                        grid[next_row][next_col] != 1):
                        continue

                    grid[next_row][next_col] = 2
                    fresh -= 1
                    queue.append((next_row, next_col))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes