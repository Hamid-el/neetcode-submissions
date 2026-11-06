# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root1, root2):
            curr1 = root1
            curr2 = root2
            if curr1 is None and curr2 is None:
                return True
            if curr1 is None or curr2 is None:
                return False
            if curr1.val != curr2.val:
                return False
            return isSameTree(curr1.left, curr2.left) and isSameTree(curr1.right, curr2.right)
        
        curr_r = root
        curr_sr = subRoot
        if curr_r is None:
            return False
        if curr_sr is None:
            return True
        if isSameTree(curr_r, curr_sr):
            return True
        return self.isSubtree(curr_r.left, curr_sr) or self.isSubtree(curr_r.right, curr_sr)