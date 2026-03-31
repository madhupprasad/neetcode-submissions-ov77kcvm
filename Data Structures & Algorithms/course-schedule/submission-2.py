class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a = {}
        for i in prerequisites:
            if i[1] in a: 
                a[i[1]].append(i[0])
            else:
                a[i[1]] = [i[0]]
        visited = set()
        print(a)
        def dfs(v):
            print('vv',v, 'visited', visited, 'a', a)
            if v not in a:
                return True
            if v in visited:
                print('done')
                return False
            visited.add(v)
            for i in a[v]:
                if not dfs(i):
                    return False
                continue
            return True
        for key in a:
            if not dfs(key):
                return False
            print('aaaaaaa')
            visited = set()
                
        
        return True