"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}

        new = head
        while new:
            copy = Node(new.val)
            d[new] = copy
            print(d[new])
            new = new.next
        new = head
        while new:
            copy = d[new]
            copy.next = d[new.next]
            copy.random = d[new.random]
            new = new.next
        
        return d[head]
