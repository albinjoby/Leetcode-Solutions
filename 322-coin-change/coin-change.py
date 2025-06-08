class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1,len(dp)):
            target = i
            for coin in coins:
                if target == coin:
                    dp[i] = 1
                else:
                    if target - coin < 0:
                        break
                    else:
                        dp[i] = min(1 + dp[i-coin], dp[i])
        
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
