class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue

                islands += 1

                # DFS and mark as visited
                stack = [(row, col)]
                grid[row][col] = "0"

                while stack:
                    curr_row, curr_col = stack.pop()

                    for row_change, col_change in directions:
                        next_row = curr_row + row_change
                        next_col = curr_col + col_change

                        if (next_row < 0 or next_row >= rows or
                            next_col < 0 or next_col >= cols or
                            grid[next_row][next_col] == "0"):
                            continue

                        grid[next_row][next_col] = "0"
                        stack.append((next_row, next_col))

        return islands