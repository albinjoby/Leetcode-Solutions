class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # recursion using memorization
        memo={(0,0):0}
        def dp(i,j):
            if i <= 0 or j <= 0:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dp(i-1,j) + dp(i,j-1)
            return memo[(i,j)]
        res = dp(m-1,n-1)
        print(memo)
        return res
