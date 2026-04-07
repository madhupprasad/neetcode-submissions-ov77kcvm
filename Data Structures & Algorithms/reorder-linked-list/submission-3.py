# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle (split the list into two halves)
        slow, fast = head, head
        while fast and fast.next:
            prev_mid = slow
            slow = slow.next
            fast = fast.next.next

        # detach first half from second
        prev_mid.next = None

        # 2. Reverse second half starting from slow
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev  # head of reversed second half

        # 3. Merge two halves
        first = head
        while first:
            tmp0 = second
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            print(first.val)
            first = tmp1
            second = tmp2
        
        tmp0.next = second
