# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curr_p = p
        curr_q = q
        if curr_p is None and curr_q is None:
            return True
        if curr_p is None or curr_q is None: # wegen rekursiven aufruf
            return False
        
        if curr_p.val != curr_q.val:
            return False
        return self.isSameTree(curr_p.left, curr_q.left) and self.isSameTree(curr_p.right, curr_q.right)