# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = head
        anotherHead = new = ListNode(0, head)
        while n > 0:
            x = x.next
            n-=1
        
        while x:
            new = new.next
            x = x.next

        new.next = new.next.next

        return anotherHead.next
        