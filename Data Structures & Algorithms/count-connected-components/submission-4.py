class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UAG adj list
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited = set()
        ok = set()
        def dfs(k, p):
            if k in ok:
                return True
            
            ok.add(k)
            for i in adjlist[k]:
                if i == p:
                    continue
                if dfs(i, k) == False:
                    return False
            return True

        c = 0
        for key in adjlist.keys():
            if key not in ok:
                dfs(key, -1)
                c+=1
        
        return c

