class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, visited):
            if (row, col) in visited:
                return

            visited.add((row, col))

            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change

                if (next_row < 0 or next_row >= rows or
                    next_col < 0 or next_col >= cols or
                    heights[next_row][next_col] < heights[row][col]):
                    continue

                dfs(next_row, next_col, visited)

        # DFS from pacific borders
        for col in range(cols):
            dfs(0, col, pacific)
        for row in range(rows):
            dfs(row, 0, pacific)

        # DFS from atlantic borders
        for col in range(cols):
            dfs(rows - 1, col, atlantic)
        for row in range(rows):
            dfs(row, cols - 1, atlantic)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result
