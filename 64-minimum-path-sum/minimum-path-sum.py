class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1)]

        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= rows or j >= cols:
                return float('inf')
            if i == rows-1 and j == cols-1:
                return grid[i][j]

            val = grid[i][j] + min(dfs(i+1,j), dfs(i,j+1))
            cache[(i,j)] = val
            return val

        return dfs(0,0)
            

            