class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i,j):
            if i >= rows or j >= cols:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = 0
            left = dfs(i+1,j)
            right = dfs(i,j+1)
            diagonal = dfs(i+1,j+1)
            if matrix[i][j] == "1":
                memo[(i,j)] = 1 + min(
                    left,right,diagonal
                )
            return memo[(i,j)]


        dfs(0,0)
        return max(memo.values()) ** 2