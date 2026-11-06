# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(root):
            curr = root
            nonlocal longest
            if curr is None:
                return 0
            
            left_depth = maxDepth(curr.left)
            right_depth = maxDepth(curr.right)
            longest = max(longest, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        
        curr = root
        longest = 0
        maxDepth(curr)
        return longest
