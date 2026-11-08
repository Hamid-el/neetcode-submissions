# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, largest_node_so_far):
            curr = root
            if curr is None:
                return 0
            
            counter = 0
            if curr.val >= largest_node_so_far:
                counter += 1
            
            largest_node_so_far = max(largest_node_so_far, curr.val)
            counter += dfs(curr.left, largest_node_so_far) 
            counter += dfs(curr.right, largest_node_so_far)
            return counter
   
        return dfs(root, float("-inf"))