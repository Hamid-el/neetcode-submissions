# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
       
        def dfs(node, level):
            curr = node
            if curr is None:
                return None
            if level == len(res):
                res.append(curr.val) # like "Binary Tree Level Order Traversal" aber immer nur ganz rechte Element soll Teil unseres Arrays sein oder in der letzigen aufgabe
            #res.append(curr.val)
            dfs(curr.right, level + 1)
            dfs(curr.left, level + 1)
        
        dfs(root, 0)
        return res