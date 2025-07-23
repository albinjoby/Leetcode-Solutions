class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {0:0}
        # def check(target: int) -> int:
        #     if target in memo:
        #         return memo[target]

        #     count = float('inf')
        #     for coin in coins:
        #         diff = target - coin
        #         if diff < 0:
        #             break
        #         count = min(count, 1 + check(diff))
            
        #     return count

        # res = check(amount)
        # return -1 if res == float('inf') else res

        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin]+1,dp[i])

        return -1 if dp[-1] == float(inf) else dp[-1]