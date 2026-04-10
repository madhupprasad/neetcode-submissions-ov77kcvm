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
        ptr = head
        prev = None
        copyMap = {}

        while ptr:
            cpy = Node(ptr.val)
            copyMap[ptr] = cpy
            ptr = ptr.next

        ptr = head

        while ptr:
            cpy = copyMap[ptr]
            cpy.next = ptr.next and copyMap[ptr.next]
            cpy.random = ptr.random and copyMap[ptr.random]
            ptr = ptr.next
        
        return copyMap[head] if head else head
