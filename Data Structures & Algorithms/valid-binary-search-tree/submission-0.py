# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minimum, maximum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            left_is_valid = dfs(node.left, minimum, node.val)
            right_is_valid = dfs(node.right, node.val, maximum)

            return left_is_valid and right_is_valid

        return dfs(root, float("-inf"), float("inf"))