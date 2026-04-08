# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = curr = head
        while curr:
            curr = curr.next
            l+=1
        t = l - n
        le = l
        l = 0
        prev = temp
        while temp:
            if l == t:
                if t == 0:
                    head = head.next
                    return head
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            l+=1
        
        return head
        