# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        def bfs(root):
            if not root:
                return
            
            from collections import deque
            q = deque([root])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    nums.append(node.val)
                
        bfs(root)
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-1):
            res = min(res, abs(nums[i]-nums[i+1]))
        
        return res