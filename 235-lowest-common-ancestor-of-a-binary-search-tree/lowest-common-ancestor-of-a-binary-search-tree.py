# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root.val
        def search(root,p,q):
            if not root:
                return 
            if root == p:
                self.res = p
                return 
            if root == q:
                self.res = q
                return 
            if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
                self.res = root
                return 
            if p.val > root.val and q.val > root.val:
                return search(root.right,p,q)
            if p.val < root.val and q.val < root.val:
                return search(root.left,p,q)
            return -1
        
        search(root,p,q)
        return self.res