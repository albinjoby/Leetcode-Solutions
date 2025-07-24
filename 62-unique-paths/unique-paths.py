class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up with tabulation

        dp = []
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)

        return dp[m-1][n-1]

        # top down with memorization
                
        # cache = {}
        # def dfs(i,j):
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     if i == 0 or j == 0:
        #         return 0
        #     if i == 1 and j == 1:
        #         return 1
        #     cache[(i,j)] = dfs(i-1,j) + dfs(i,j-1)
        #     return cache[(i,j)]

        # return dfs(m,n)