class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1:
                return 0
            
            temp = grid[r][c]
            grid[r][c] = 3
            s = dfs(r + 1, c) + dfs(r -1, c) + dfs(r, c+1) + dfs(r, c -1) + 1
            return s
        res = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res.append(dfs(r,c))
        if len(res) == 0:
            return 0
        return max(res)