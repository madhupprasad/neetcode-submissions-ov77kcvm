class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n_nodes = len(edges) + 1
        n = []
        adj = {}
        for i in range(n_nodes):
            n.append(0)
            adj[i] = []
        
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
            n[u]+=1
            n[v]+=1
        print(n, adj)
        q = deque()
        for i in range(len(n)):
            if n[i] == 1:
                q.append(i)
        print(q)
        while q:
            v = q.popleft()
            n[v]-=1

            for i in adj[v]:
                n[i]-=1
                if n[i] == 1:
                    q.append(i)
        ans = set()
        for i in range(len(n)):
            if n[i] == 2:
                ans.add(i)
        
        for u,v in reversed(edges):
            if u in ans and v in ans:
                return [u,v]
