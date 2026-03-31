class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        move = [[0,1],[1,0],[0,-1],[-1,0]]
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    st = []
                    st.append([i,j])
                    area = 0
                    grid[i][j] = 'v'
                    while st:
                        i,j = st.pop()
                        area += 1
                        print(i,j, area)
                        for m in move:
                            di,dj = i+m[0], j+m[1]
                            if di < 0 or di >= rows or dj < 0 or dj >= cols or grid[di][dj] != 1:
                                continue
                            grid[di][dj] = 'v'
                            st.append([di,dj])
                
                    max_area = area if area > max_area else max_area
        
        return max_area


