class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def iter(i,j):
            st = [(i,j)]

            while st:
                ri, cj = st.pop()

                if ri < 0 or cj < 0 or ri >= len(grid) or cj >= len(grid[0]):
                    continue
                
                if grid[ri][cj] != "1":
                    continue

                grid[ri][cj] = "#"

                st.append((ri + 1, cj))  # down
                st.append((ri - 1, cj))  # up
                st.append((ri, cj + 1))  # right
                st.append((ri, cj - 1))  # left


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    iter(i,j)
        
        return count

                    
                    