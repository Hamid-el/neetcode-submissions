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
        # hashmap[None] wouldnt work, returns error but not with h.get(...), so 
        # {None: None} would be needed
        h = {} 
        curr = head

        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            h[curr].next = h.get(curr.next)
            h[curr].random = h.get(curr.random)

            curr = curr.next

        return h.get(head)