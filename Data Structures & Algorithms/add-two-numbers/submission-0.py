# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        num1 = 0
        pos1 = 0
        while curr1:
            num1 += curr1.val * (10 ** pos1)
            pos1 += 1
            curr1 = curr1.next
        
        curr2 = l2
        num2 = 0
        pos2 = 0
        while curr2:
            num2 += curr2.val * (10 ** pos2)
            pos2 += 1
            curr2 = curr2.next
        
        num = num1 + num2
        l3 = ListNode()
        curr = l3
        while num > 0  or curr == l3:
           digit = num % 10
           num //= 10
           curr.next = ListNode(digit)
           curr = curr.next 

        return l3.next