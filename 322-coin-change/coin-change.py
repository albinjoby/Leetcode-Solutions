class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0:0}
        coins.sort()

        def top_down(money):
            if money in cache:
                return cache[money]
            
            res = float('inf')
            for coin in coins:
                diff = money - coin
                if diff < 0:
                    break

                res = min(res,1+top_down(diff))
            
            cache[money] = res
            return res

        res = top_down(amount)
        return -1 if res == float('inf') else res
                
