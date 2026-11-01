# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        slow = curr
        fast = curr
        
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # middle is at slow now, so split+reverse second half
        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:    
            nxt = curr.next # n eins nach vorne
            curr.next = prev # umdrehen -----|
            prev = curr # p eins nach vorne  |
            curr = nxt # c eins nach vorne   dann verschieben
        second = prev # new head

        curr_first = head
        curr_second = second
        while curr_second:
            nxt_first = curr_first.next
            nxt_second = curr_second.next

            curr_first.next = curr_second
            curr_second.next = nxt_first

            curr_first = nxt_first
            curr_second = nxt_second

        return None
