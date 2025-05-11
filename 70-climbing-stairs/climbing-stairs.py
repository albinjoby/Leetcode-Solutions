class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+2)
        dp[1] = 1
        i = 2
        while i < len(dp):
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[-1]