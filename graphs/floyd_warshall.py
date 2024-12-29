class FloodFill:
    def run(self, grid, x, y, new_color):
        original_color = grid[x][y]
        if original_color == new_color:
            return grid

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != original_color:
                return
            grid[x][y] = new_color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(x, y)
        return grid