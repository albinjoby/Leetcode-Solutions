class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        # recursion using memorization
        # n = len(cost)
        # memo = {}
        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     if n <= 0:
        #         return 0
        #     memo[n] = cost[n-1] + min(dp(n-1),dp(n-2))
        #     return memo[n]
        # return min(dp(n),dp(n-1))

        # iteration using tabulation
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        return min(dp[-1],dp[-2])
