# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        import heapq
        res = []
        heapq.heapify(res)
        def dfs(root):
            if not root:
                return 
            heapq.heappush(res,-root.val)
            while len(res) > k:
                heapq.heappop(res)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return -res[0]