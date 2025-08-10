# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l_node,r_node):
            if not l_node and not r_node:
                return True
            
            if not l_node or not r_node:
                return False

            return l_node.val == r_node.val and dfs(l_node.left,r_node.right) and dfs(l_node.right,r_node.left)

        return dfs(root.left,root.right) if root else True
            