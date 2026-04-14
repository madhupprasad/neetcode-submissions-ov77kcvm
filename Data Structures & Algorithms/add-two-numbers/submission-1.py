# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse
        t1 = l1
        t2 = l2
        tsol = sol = ListNode(0)
        carry = 0
        while t1 or t2:
            isum = (t1.val if t1 else 0) + (t2.val if t2 else 0)+carry
            if isum >= 10:
                vsum = isum%10
            else:
                vsum = isum
            
            new = ListNode(0)
            new.val = vsum
            carry = isum//10 if isum >= 10 else 0
            tsol.next = new
            tsol = new
            t1 = t1 and t1.next
            t2 = t2 and t2.next
        if carry:
            new = ListNode(carry)
            tsol.next = new
        return sol.next

