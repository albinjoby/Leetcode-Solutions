"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dic = {}

        seen = set()
        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            dic[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)
            
        dfs(node)
        seen = set()
        def connect(node):
            if node in seen:
                return 
            seen.add(node)
            for nei in node.neighbors:
                dic[node].neighbors.append(dic[nei])
                connect(nei)
        
        connect(node)
        return dic[node]
