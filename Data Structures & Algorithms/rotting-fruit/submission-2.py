class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        q = []
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if not fresh:
            return 0
        t = 0        
        while q:
            temp = []
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                for i, j in q:
                    ni = i + di
                    nj = j + dj

                    if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] == 1:
                        temp.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1

            q = temp
            t += 1

        return t - 1 if not fresh else -1
