# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(start, end):
            prev = end
            curr = start

            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check whether k nodes are available
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            group_head = group_prev.next

            # reverse curr group
            new_head = reverse(group_head, group_next)

            # reconnect reversed group
            group_prev.next = new_head
            group_prev = group_head