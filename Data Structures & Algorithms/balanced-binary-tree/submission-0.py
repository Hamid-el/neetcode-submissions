# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def maxDepth(root):
            curr = root
            nonlocal balanced
            if curr is None:
                return 0
            
            left_depth = maxDepth(curr.left)
            right_depth = maxDepth(curr.right)
            if not (-1 <= left_depth - right_depth <= 1):
                balanced = False
            return 1 + max(left_depth, right_depth)

        balanced = True
        maxDepth(root)
        return balanced