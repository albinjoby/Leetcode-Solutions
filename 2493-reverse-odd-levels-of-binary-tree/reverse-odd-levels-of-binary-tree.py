# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        if not root:
            return root

        q = deque([root])
        level = 0

        while q:
            size = len(q)
            current_level = []

            for _ in range(size):
                node = q.popleft()
                current_level.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                values = [node.val for node in current_level]
                values.reverse()

                for i, node in enumerate(current_level):
                    node.val = values[i]

            level += 1

        return root