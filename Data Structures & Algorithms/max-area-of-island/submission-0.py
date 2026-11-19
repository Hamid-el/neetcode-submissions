class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                area = 0

                # DFS and mark as visited
                stack = [(row, col)]
                grid[row][col] = 0

                while stack:
                    curr_row, curr_col = stack.pop()

                    area += 1

                    for row_change, col_change in directions:
                        next_row = curr_row + row_change
                        next_col = curr_col + col_change

                        if (next_row < 0 or next_row >= rows or
                            next_col < 0 or next_col >= cols or
                            grid[next_row][next_col] == 0):
                            continue

                        grid[next_row][next_col] = 0
                        stack.append((next_row, next_col))

                max_area = max(max_area, area)

        return max_area