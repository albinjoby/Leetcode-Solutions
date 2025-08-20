class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(i,j):
            if i >= rows or j >= cols or matrix[i][j] == 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = 1 + min(
                dfs(i+1,j),
                dfs(i,j+1),
                dfs(i+1,j+1)
            )
            return memo[(i,j)]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res += dfs(i,j)
        
        return res