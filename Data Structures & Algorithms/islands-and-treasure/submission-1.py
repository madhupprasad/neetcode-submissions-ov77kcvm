class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        movements = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c,l):
            q = deque()
            q.append((r,c,l))
            visited = set()
            while q:
                r,c,l = q.popleft()
                visited.add((r,c))
                if grid[r][c] == 0:
                    return l
                for i in movements:
                    R = r+i[0]
                    C = c+i[1]
                    if R < 0 or R >= rows or C < 0 or C >= cols:
                        continue
                    if (R, C) in visited:
                        continue
                    if grid[R][C] != -1:
                        q.append((R, C, l+1))    
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j,0)