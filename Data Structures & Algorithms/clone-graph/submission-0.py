"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}

        def dfs(curr):
            if curr in maps:
                return maps[curr]
            copy = Node(curr.val)
            maps[curr] = copy
            for n in curr.neighbors:
                v = dfs(n)
                copy.neighbors.append(v)
            return copy
        return dfs(node)