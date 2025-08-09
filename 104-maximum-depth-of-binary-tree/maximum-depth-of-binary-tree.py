# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left),dfs(root.right))
        
        # return dfs(root)

        from collections import deque
        def bfs(root):
            if not root:
                return 0

            lvl = 0
            q = deque([root])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                lvl += 1
            return lvl
        
        return bfs(root)