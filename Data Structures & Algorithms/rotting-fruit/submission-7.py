class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        q = deque()

        fr = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    fr += 1
        
        if fr == 0:
            return 0
                    
        # the q has all the rotten orange as level 0

        neigh = [(0,1),(1, 0),(0,-1),(-1,0)]
        level = 0
        while q:
            i,j,l = q.popleft()
            level = l
            for n in neigh:
                di, dj = i+n[0], j+n[1]

                if di < 0 or di >= row or dj < 0 or dj >= col or grid[di][dj] != 1:
                    continue
                
                if grid[di][dj] == 1:
                    q.append((di,dj,l+1))
                    grid[di][dj] = 2 
                    fr -= 1
                            
        if fr != 0:
            return -1
        else:
            return level