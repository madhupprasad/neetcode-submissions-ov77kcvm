class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        a = {}
        for i in range(numCourses):
            a[i] = []
        for k,v in prerequisites:
            a[k].append(v)
        visited = set()
        cycle = set()
        out = []

        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False
            cycle.add(c)
            for i in a[c]:
                if dfs(i) == False:
                    return False
            visited.add(c)
            out.append(c)
            return True

        
        for i in range(numCourses):
            if dfs(i) is False:
                return []
            cycle = set()

        return out