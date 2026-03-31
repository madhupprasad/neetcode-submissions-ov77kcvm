class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        border = []
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0 or i == r-1 or j == c-1:
                    border.append([i,j])

        moves = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(i,j,v):
            visited.add((i,j))
            for m in moves:
                di,dj = i + m[0], j + m[1]
                if di < 0 or di >= r or dj < 0 or dj >= c or board[di][dj] == 'X' or (di,dj) in visited:
                    continue
                dfs(di,dj,visited)
            
            return visited
                
        visited = set()
        for i,j in border:
            if board[i][j] == 'O': 
                v = set()   
                visited.update(dfs(i,j,v))
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited:
                    board[i][j] = 'X'