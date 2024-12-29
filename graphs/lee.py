from collections import deque

class Lee:
    def run(self, grid, start, end):
        rows, cols = len(grid), len(grid[0])
        
        if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
            return -1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(*start, 0)])
        
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, dist = queue.popleft()

            if (x, y) == end:
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True

        return -1

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    lee_algorithm = Lee()
    result = lee_algorithm.run(grid, start, end)
    print("Panjang jalur terpendek:", result)