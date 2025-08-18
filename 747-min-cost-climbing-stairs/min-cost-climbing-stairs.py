class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        n = len(cost)
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n <= 0:
                return 0
            memo[n] = cost[n-1] + min(dp(n-1),dp(n-2))
            return memo[n]
        return min(dp(n),dp(n-1))