class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        cache = {0:0}
        def min_coins(target):
            if target in cache:
                return cache[target]
            
            count = float('inf')
            for coin in coins:
                diff = target - coin
                if diff < 0:
                    break
                count = min(count, 1 + min_coins(diff))
            cache[target] = count
            return cache[target]
            

        res = min_coins(amount)
        return -1 if res == float('inf') else res
