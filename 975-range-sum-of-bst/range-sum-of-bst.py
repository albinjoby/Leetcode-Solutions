# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def bst(root):
            if not root:
                return
            
            if low <= root.val <= high:
                arr.append(root.val)
            
            if root.val >= low:
                bst(root.left)
            if root.val <= high:
                bst(root.right)

        bst(root)
        return sum(arr)
