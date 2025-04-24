# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []

            res = []
            temp = []
            q = deque([root])
            while q:
                l = len(q)
                for i in range(l):
                    node = q.popleft()
                    temp.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(temp)
                temp = []

            return res

        return bfs(root)