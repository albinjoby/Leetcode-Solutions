class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # recursion using memorization
        # memo={(0,0):0}
        # def dp(i,j):
        #     if i <= 0 or j <= 0:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     memo[(i,j)] = dp(i-1,j) + dp(i,j-1)
        #     return memo[(i,j)]
        # return dp(m-1,n-1)

        # iteration using tabulation
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        print(dp)
        for i in range(m):
            for j in range(n):
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j] 
        return dp[m-1][n-1]