class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        
        def bfs(starts):
            reachable = set(starts)
            queue = collections.deque(starts)
            while queue:
                i, j = queue.popleft()
                for m in [(0,1),(1,0),(0,-1),(-1,0)]:
                    di, dj = i + m[0], j + m[1]
                    if 0 <= di < r and 0 <= dj < c and (di, dj) not in reachable and heights[di][dj] >= heights[i][j]:
                        reachable.add((di, dj))
                        queue.append((di, dj))
            return reachable

        pacific_starts = []
        atlantic_starts = []
        for i in range(r):
            pacific_starts.append((i, 0))
            atlantic_starts.append((i, c - 1))
        for j in range(c):
            pacific_starts.append((0, j))
            atlantic_starts.append((r - 1, j))
            
        p_set = bfs(pacific_starts)
        a_set = bfs(atlantic_starts)
        
        res = []
        for i, j in p_set:
            if (i, j) in a_set:
                res.append([i, j])
        return res