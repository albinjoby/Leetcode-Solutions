# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,count):
            if not root:
                return count
            return 1+max(dfs(root.left,count),dfs(root.right,count))
        
        return dfs(root,0)